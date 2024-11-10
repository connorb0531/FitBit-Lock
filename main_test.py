import os
from dotenv import load_dotenv
from api_requests import make_fitbit_request

load_dotenv()

# Access environment variables
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
TOKEN_FILE = os.getenv('TOKEN_FILE')

distance = ['/1/user/-/activities/distance/date/today/today/1sec.json', 'activities-distance']
steps = ['/1/user/-/activities/steps/date/today/today/1sec.json', 'activities-steps']
calories = ['/1/user/-/activities/calories/date/today/today/1sec.json', 'activities-calories']

CALORIE_GOAL = 1606


def get_data(data_type):
    json_request_endpoint = data_type[0]
    endpoint_url = f'https://api.fitbit.com{json_request_endpoint}'
    response = make_fitbit_request(endpoint_url)

    if response.status_code == 200:
        json_data = response.json()

        target_data = json_data[data_type[1]][0]['value']

        return target_data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return -1


distance_value = round(float(get_data(distance)) * 0.62137, 2)
steps_value = get_data(steps)
calories_value = get_data(calories)

print(f'distance: {distance_value}')
print(f'steps: {steps_value}')
print(f'calories: {calories_value}')
