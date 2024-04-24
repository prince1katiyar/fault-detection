from sensor.config import mongo_client
import pandas as pd 
import logging
import json


def dump_csv_file_to_mongodb_collecton(file_path:str,database_name:str,collection_name:str)->None:
    try:
        df = pd.read_csv(file_path)
        logging.info(f"rows and column {df.shape}")

        df.reset_index(drop=True,inplace=True)
        json_records=list(json.loads(df.T.to_json()).values())

        mongo_client[database_name][collection_name].insert_many(json_records)
    except Exception as e : 
        print(e)



"""  
.env
aps file insert
sensr : __init__ file for laoding env
utils file  for dumping data into database
config for reading mongodb url 
"""


"""
main for running 
entity - config for creating folder realted to data ingestion
in training init _ all tle constant for trainning is kept there 
in config put the schemas over there 




we crete training pipeline and
artrifacts we put code
then run the pipeline 
"""