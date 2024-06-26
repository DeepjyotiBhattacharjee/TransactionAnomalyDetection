import sys
from src.Transaction_Anomaly_Detection.logger import logging
from src.Transaction_Anomaly_Detection.exception import CustomException
from src.Transaction_Anomaly_Detection.components.data_ingestion import DataIngestion, DataIngestionConfig

if __name__=="__main__":
    logging.info("The execution has started...")

    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom exception...")
        raise CustomException(e,sys)