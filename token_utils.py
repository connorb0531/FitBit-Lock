import json
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_FILE = os.getenv('TOKEN_FILE')


def load_tokens():
    try:
        with open(TOKEN_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def save_tokens(tokens):
    with open(TOKEN_FILE, 'w') as file:
        json.dump(tokens, file)


