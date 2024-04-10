from sensor.configuration.mongodb_db_connection import MongoDBClient



if __name__ =='__main__':
    mongodb_client = MongoDBClient()
   # print(mongodb_client)
    print("collection name:" ,mongodb_client.database.list_collection_names())