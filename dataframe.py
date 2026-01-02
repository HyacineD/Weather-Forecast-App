import pandas as pd
import os , sys
from extract import archive,forecast
class DataFrame:
    def __init__(self,forecast_data):
        self.archive_data=pd.read_csv(os.path.join(sys.path[0],'data_weather.csv'))
        # self.archive_data['time']=pd.to_datetime(self.archive_data['time'])
        self.archive_data=self.to_dataframe(self.archive_data)

        self.forecast_data=self.to_dataframe(forecast_data)

    def to_dataframe(self,data):
        if isinstance(data , DataFrame):
            pass
        else:
            df=pd.DataFrame(data)
        df['time']=pd.to_datetime(df['time'])
        df['date']=df['time'].dt.date
        df['jour']=df['time'].dt.day
        df['mois']=df['time'].dt.month
        df['annee']=df['time'].dt.year
        # df.set_index('time',inplac:e=True)
        return df
    def date(self):
        self.df['time']=pd.to_datetime(self.df['time'])
        
        return self.df
    def concatenate_data(self):
        df_all=pd.concat([self.archive_data,self.forecast_data],ignore_index=True)
        df_all.drop_duplicates(subset=['time'], inplace=True)
        df_all.set_index('time',inplace=True)
        df_all.sort_index(inplace=True)
        df_all.to_csv(os.path.join(sys.path[0],'data_weather_full.csv'))
        return df_all

    
    def save_to_csv(self,filename):
        csv_path=os.path.join(sys.path[0],filename)
        df=self.to_dataframe()
        df.to_csv(csv_path,index=False)
        return csv_path
