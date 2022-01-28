import os

from dotenv import load_dotenv

load_dotenv()

SLACK_URL = os.getenv('SLACK_URL')
