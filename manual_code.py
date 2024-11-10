from dotenv import load_dotenv
import os
import webbrowser
from flask import Flask

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')
TOKEN_FILE = os.getenv('TOKEN_FILE')

app = Flask(__name__)

# Main function to open browser and start the Flask server (local)
if __name__ == '__main__':
    # Step 1: Open Fitbit authorization URL in the default browser
    auth_url = (f'https://www.fitbit.com/oauth2/authorize?response_type=code&client_id={CLIENT_ID}'
                f'&redirect_uri={REDIRECT_URI}&scope=activity%20heartrate%20profile')
    print(f"Opening authorization URL: {auth_url}")
    webbrowser.open(auth_url)

    app.run(port=8080)

    # Step 2: Replace AUTH_CODE in env file with code found within url
    # Step 3: Run init_token_save.py for initialize main and refresh tokens
