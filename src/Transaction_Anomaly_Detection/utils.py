import os
import sys
from src.Transaction_Anomaly_Detection.exception import CustomException
from src.Transaction_Anomaly_Detection.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL data started...")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection established ")
        df = pd.read_sql_query('SELECT * FROM transaction_anomalies_dataset',mydb)
        print(df.head())
        return df
    except Exception as e:
        raise CustomException(e,sys)