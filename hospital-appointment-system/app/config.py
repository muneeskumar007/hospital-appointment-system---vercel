
import os

def get_db_connection():
    # For Vercel PostgreSQL
    database_url = os.getenv('DATABASE_URL')
    if database_url:
        return database_url
    # Fallback for local development
    return "postgresql://user:password@localhost/hospital_db"