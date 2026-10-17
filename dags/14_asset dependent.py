from airflow.sdk import dag,task,asset
from pendulum import datetime
from asset import fetch_data
import os

@asset(
    schedule=fetch_data,
    uri="/opt/airflow/logs/data/data_processed.txt",
    name="process_data"

)
def process_data(self):
    #ensure the directory exits
    os.makedirs(os.path.dirname(self.uri),exist_ok=True)

    #simulate data processed by writing to a file

    with open(self.uri,'w')as f:
        f.write(f"Data processed successfully")

    print(f"Data processed to {self.uri}")