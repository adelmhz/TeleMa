import os

class Settings:
    API_TOKEN = os.environ.get('API_TOKEN')

settings = Settings()