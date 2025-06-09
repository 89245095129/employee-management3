# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# config.py
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mysecretpassword@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
