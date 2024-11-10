# Fitbit Lock Project

## Overview

The Fitbit Lock Project integrates Fitbit's API with a physical lock, enabling users to unlock a door when specific fitness goals are reached (e.g., distance, steps, calories). The system retrieves Fitbit activity data through API requests and controls a physical lock using a Raspberry Pi.

## Features

- **Authentication and Token Management**: Handles the OAuth2 authorization process with Fitbit's API.
- **Data Retrieval**: Fetches user activity data (e.g., distance, steps, calories).
- **Goal Tracking**: Monitors fitness metrics and checks progress against user-defined goals.
- **Relay Control**: Unlocks a door when goals are achieved and locks it afterward.

## Requirements

- **Python 3.8+**
- **Fitbit Developer Account**
  https://dev.fitbit.com/build/reference/
- **Raspberry Pi** (or any device with GPIO support)
- **Fitbit Watch Device** (for data tracking)
- **Relay Module**
- **Lock**
- **Environment Variables**:
  - `CLIENT_ID`
  - `CLIENT_SECRET`
  - `AUTH_CODE`
  - `LOCK_PIN`
  - `REFRESH_INTERVAL`

## Usage

### 1. Authentication

Run `manual_code.py` to start the local Flask server and open the Fitbit authorization page in your browser:
   ```bash
   python manual_code.py
   ```
ENSURE `CLIENT_ID` and `CLIENT_SECRET` are entered in `.env` or you won't get the correct URL


- Get the authorization code from the redirected URL.
- Save the `AUTH_CODE` in your `.env` file.
- Example URL: http://localhost/?code=9800b30662814810875cc1d84afa47346c15280d#_=_
- The `AUTH_CODE` would be `9800b30662814810875cc1d84afa47346c15280d`


### 2. Token Initialization

Run `init_token_save.py` to exchange the authorization code for access and refresh tokens:
   ```bash
   python init_token_save.py
   ```

### 3. Main Tracking Script

Run `main.py` to start tracking selected data (distance, steps, calories) and control the lock:
   ```bash
   python main.py
   ```
- Choose the data type and set a target when prompted.

## Hardware Setup

- Connect the relay module to the Raspberry Pi GPIO pin specified in `LOCK_PIN`.
- Connect lock to relay 

## Security and Best Practices

- **API Limits**: Be mindful of Fitbit's API rate limits (150 requests per hour).

## Troubleshooting

- **Token Expiration**: If you encounter a `401 Unauthorized` error, ensure the refresh token is valid. Run `manual_code.py` to obtain new `AUTH_CODE` and run `python init_token_save.py`
- **Environment Errors**: Double-check that all required variables are set in the `.env` file.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.


## Acknowledgements

- Fitbit API documentation
- Python libraries: `requests`, `dotenv`, `gpiozero`

