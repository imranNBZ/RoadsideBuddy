import os

class Config:
    # Firebase Setup
    FIREBASE_CREDENTIALS = os.getenv('FIREBASE_CREDENTIALS', 'codeAndTests/firebase/roadsidebuddy-35064-firebase-adminsdk-fbsvc-99d790f84b.json')
    FIREBASE_DATABASE_URL = os.getenv("FIREBASE_DATABASE_URL", "https://roadsidebuddy-35064-default-rtdb.firebaseio.com/")

    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "its-a-secret-key")

    # PostgreSQL (Render Database)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # Ensure this is set in Render
    SQLALCHEMY_TRACK_MODIFICATIONS = False

 

    # ClickSend API
    CLICKSEND_USERNAME = os.getenv("CLICKSEND_USERNAME", "")
    CLICKSEND_API_KEY = os.getenv("CLICKSEND_API_KEY", "")

    # SMTP Email Configuration
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    SMTP_EMAIL = os.getenv('SMTP_EMAIL', 'admin@example.com')  # Admin email
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', 'yourpassword')  # App-specific password
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@example.com')  # Recipient (admin) email


Config = Config()