import os
import time
from api_requests import make_fitbit_request
from datetime import datetime
from dotenv import load_dotenv
from relay_lock_control import timed_unlock, lock_door

load_dotenv()

# API Request time interval. FitBit Api offers 150 requests/hour
REFRESH_INTERVAL = int(os.getenv('REFRESH_INTERVAL'))

# 3 choices of data obtained
data_types = {
    '1': ['/1/user/-/activities/distance/date/today/today/1sec.json', 'activities-distance', 'Distance'],
    '2': ['/1/user/-/activities/steps/date/today/today/1sec.json', 'activities-steps', 'Steps'],
    '3': ['/1/user/-/activities/calories/date/today/today/1sec.json', 'activities-calories', 'Calories']
}


# Returns value of specified data & and data name
def get_data(data_type):
    json_request_endpoint = data_type[0]
    endpoint_url = f'https://api.fitbit.com{json_request_endpoint}'
    response = make_fitbit_request(endpoint_url)

    if response.status_code == 200:
        json_data = response.json()

        target_data = json_data[data_type[1]][0]['value']

        return float(target_data), data_type[2]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return -1, 'null'


# Menu for selecting data type
def menu():
    print("Select the data type you want to track:")
    print("1. Distance")
    print("2. Steps")
    print("3. Calories")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice in data_types:
        selection = data_types[choice]
        try:
            target = float(input("Enter target to track: ").strip())
            lock_door()
            start_tracking(selection, target)
        except ValueError:
            print("Invalid target value. Please enter a valid number.")
    else:
        print("Invalid choice. Please restart and select 1, 2, or 3.")


# Retrieve data value every REFRESH_INTERVAL seconds
def start_tracking(selection, target):
    while True:
        value, name = get_data(selection)

        if name == 'Distance':
            value = round(float(value * 0.62137), 2)

        current_time = datetime.now().strftime('%H:%M:%S')

        # Check if the goal has been reached
        if value >= target:
            print(f'{current_time}: Goal reached for {name}.')
            timed_unlock()
            break
        else:
            print(f'{current_time}: Goal not reached for {name}\n'
                  f'\tCurrent value: {value}. Target: {target}\n'
                  f'\tRefreshing in {REFRESH_INTERVAL} seconds...')

        time.sleep(REFRESH_INTERVAL)


if __name__ == '__main__':
    while True:
        menu()
