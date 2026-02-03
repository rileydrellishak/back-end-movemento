import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

    OCI_REGION = os.getenv("OCI_REGION")
    OCI_NAMESPACE = os.getenv('OCI_NAMESPACE')
    OCI_BUCKET_NAME = os.getenv('OCI_BUCKET_NAME')
    OCI_PAR_EXPIRATION_MINUTES = int(os.getenv('OCI_PAR_EXPIRATION_MINUTES', 5))