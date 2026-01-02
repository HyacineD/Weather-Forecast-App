import pandas as pd
from dataframe import DataFrame
import os , sys
from split_time import split_period
import csv
def df_archive_to_csv(start_date:str,end_date:str,data,filename:str="data_weather.csv")->str:
    if os.path.exists(os.path.join(sys.path[0],filename)):
        print(f"Le fichier {filename} existe déjà.")
        df = pd.DataFrame(data)
        df.to_csv(os.path.join(sys.path[0],filename), mode='a', header=False, index=False)
    else:
        print(f"Le fichier {filename} n'existe pas. Création d'un nouveau fichier.")
        csv_path=os.path.join(sys.path[0],filename)
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        df = pd.DataFrame(data)
        df.to_csv(csv_path, mode='w', header=True, index=False)
    return 
            