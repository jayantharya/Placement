import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    try:
        uri = os.environ.get("MONGO_URI")
        
        if not uri:
            print("Error: MONGO_URI not found in .env file.")
            return None

        client = MongoClient(uri, tlsCAFile=certifi.where())
        
        client.admin.command('ping')
        print("Success! Connected securely to the cluster.")
        return client["Bank"]
        
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None


if __name__ == "__main__":
    db = connect_db()