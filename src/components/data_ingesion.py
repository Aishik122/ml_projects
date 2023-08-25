import os 
import sys 
from src.exception import Custom_Exception
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation 
from src.components.data_transformation import DataTransformationConfig

@dataclass
class DataIngesionConfig:
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','data.csv')
class DataIngesion:
    def __init__ (self):
        self.ingesionconfig = DataIngesionConfig()
    def initiate_data_ingestion(self):
        logging.info("enter the data ingestion method and component ")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("read the data as dataframe")
            os.makedirs(os.path.dirname(self.ingesionconfig.train_data_path),exist_ok=True)
            
            df.to_csv(self.ingesionconfig.raw_data_path,index=False,header=True)
            logging.info("Train_test_split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingesionconfig.train_data_path)
            test_set.to_csv(self.ingesionconfig.test_data_path)
            logging.info("Ingestion of the data is completed")
            
            return (
                self.ingesionconfig.train_data_path,
                self.ingesionconfig.test_data_path
                
            )
                       
        except Exception as e:
            raise Custom_Exception(e,sys)
if __name__ == "__main__":
    obj=DataIngesion()
    train_data,test_data= obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)