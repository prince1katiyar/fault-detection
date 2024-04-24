from dotenv import load_dotenv
import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Constants
MONGODB_URL_KEY = "MONGO_DB_URL"  # Replace with the correct key from your .env file

# Retrieve CA certificate file path
ca = certifi.where()

class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                logging.info(f"Retrieved MongoDB URL: {mongo_db_url}")

                if "localhost" in mongo_db_url:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
                
                # Check MongoDB client connection status
                if MongoDBClient.client.server_info():
                    logging.info("Successfully connected to MongoDB server")
                else:
                    logging.error("Failed to connect to MongoDB server")
                    raise Exception("Failed to connect to MongoDB server")

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            logging.error(f"Error initializing MongoDB client: {e}")
            raise

# Test MongoDBClient class
if __name__ == "__main__":
    try:
        mongo_client = MongoDBClient()
        logging.info("MongoDB client initialized successfully")
    except Exception as e:
        logging.error(f"Error initializing MongoDB client: {e}")
