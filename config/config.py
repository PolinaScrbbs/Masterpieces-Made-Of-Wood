from dotenv import load_dotenv
import os

os.environ.pop('SECRET_KEY', None)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

