import requests
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from token_utils import load_tokens, save_tokens

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def refresh_access_token(refresh_token):
    token_url = 'https://api.fitbit.com/oauth2/token'

    response = requests.post(
        token_url,
        data={
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
        },
        auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    )

    if response.status_code == 200:
        new_tokens = response.json()
        save_tokens(new_tokens)  # Save the new tokens to file
        return new_tokens['access_token']
    else:
        raise Exception(f"Error refreshing token: {response.status_code} - {response.text}")


def make_fitbit_request(endpoint):
    tokens = load_tokens()
    if not tokens:
        raise Exception("No tokens found. You need to authenticate first.")

    access_token = tokens['access_token']
    refresh_token = tokens['refresh_token']

    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Make the API request
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 401:  # Access token expired
        print("Access token expired. Refreshing...")
        access_token = refresh_access_token(refresh_token)

        # Retry the request with the new access token
        headers['Authorization'] = f'Bearer {access_token}'
        response = requests.get(endpoint, headers=headers)

    return response
