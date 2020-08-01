import requests
import json
import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(""))

from config import user_key

def mountain ():
    private_key = user_key()
    route_id = '108471503' #want to randomize this
    base_url = 'https://www.mountainproject.com/data/get-routes?routeIds='

    #Mountain Project REST API get request and response
    request_url = base_url + route_id + '&key=' + private_key
    my_request = requests.get(request_url)

    raw_response = json.loads(my_request.content)
    raw_response.keys()
    mountain_df = pd.json_normalize(raw_response['routes'])
    #print(mountain_df)
    #Specifying the variables from the data frame
    climb_name = mountain_df['name'].iloc[0]
    climb_type = mountain_df['type'].iloc[0]
    climb_rating = mountain_df['rating'].iloc[0]
    climb_stars = mountain_df['stars'].iloc[0]
    climb_url = mountain_df['url'].iloc[0]
    climb_image = mountain_df['imgMedium'].iloc[0]

    #Breaks out the climbing location variables
    climb_location = mountain_df['location'].iloc[0]
    climb_state = climb_location[0]
    climb_city = climb_location[1]
    #climb_area_1 = climb_location[2]
    #climb_area_2 = climb_location[3]
    #climb_area_3 = climb_location[4]

    message = 'Random Route of the day goes to ' + climb_name + ' in ' + climb_city + ', ' + climb_state + '. This is a ' + climb_type + ' route with a difficulty rating of ' + climb_rating + '. Check out the link for more details. Climb on!'
    print(message)

mountain()