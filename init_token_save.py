import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
TOKEN_FILE = os.getenv('TOKEN_FILE')
AUTH_CODE = os.getenv('AUTH_CODE')  # Replace with your actual code


# Function to exchange the authorization code for access and refresh tokens
def exchange_auth_code_for_tokens(auth_code):
    token_url = 'https://api.fitbit.com/oauth2/token'

    response = requests.post(
        token_url,
        data={
            'client_id': CLIENT_ID,
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'code': auth_code,
        },
        auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    )

    if response.status_code == 200:
        tokens = response.json()
        with open(TOKEN_FILE, 'w') as file:
            file.write(response.text)  # Save tokens to file
        print("Tokens saved successfully!")
        print(f"Access Token: {tokens['access_token']}")
        print(f"Refresh Token: {tokens['refresh_token']}")
    else:
        print(f"Error retrieving tokens: {response.status_code} - {response.text}")


# Exchange the authorization code for tokens
exchange_auth_code_for_tokens(AUTH_CODE)
