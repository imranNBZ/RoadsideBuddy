import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Firebase Setup
    FIREBASE_CREDENTIALS = os.getenv('FIREBASE_CREDENTIALS')

    # Debugging: Check if the file exists
    if not FIREBASE_CREDENTIALS or not os.path.exists(FIREBASE_CREDENTIALS):
        raise FileNotFoundError(f"Firebase credentials file not found: {FIREBASE_CREDENTIALS}")

    FIREBASE_DATABASE_URL = os.getenv("FIREBASE_DATABASE_URL", "https://roadsidebuddy-35064-default-rtdb.firebaseio.com/")

    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "its-a-secret-key")

    # PostgreSQL
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://localhost/roadsidebuddy")
    if DATABASE_URL.startswith("postgres://"):  
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False




Config = Config()
