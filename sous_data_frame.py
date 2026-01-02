from dataframe import DataFrame
import pandas as pd
import os , sys
from abc import ABC, abstractmethod
from extract import archive,forecast
import csv

class SousDataFrame(ABC):
    def __init__(self,dataframe:DataFrame):
        if os.path.exists(os.path.join(sys.path[0], "data_weather_full.csv")):
            self.dataframe=pd.read_csv(os.path.join(sys.path[0], "data_weather_full.csv"))
            self.df=self.dataframe
        else :
            if dataframe is None:
                archive_data=archive(latitude="36.7538",longitude="3.0588").fetch_data()

            
                forecast_data=forecast(latitude="36.7538",longitude="3.0588").fetch_data()
                dataframe=DataFrame(forecast_data)

                self.dataframe=dataframe
                self.df=self.dataframe.concatenate_data()
        self.target_column=None
    @abstractmethod
    def feature_engineering(self):
        pass
    def df_date(self):
        df_date=self.df[['date','jour','mois','annee']]
        return df_date
    @abstractmethod
    def get_target_column(self):
        pass
    @abstractmethod
    def ajouter_une_ligne(self):
        max=self.df['date'].max()+pd.Timedelta(days=1)
        self.df.loc[len(self.df)] = {col : (max if col == 'date' else None) for col in self.df.columns}
        if os.path.join(sys.path[0],(f'{self.target_column}_data_frame.csv')):
            self.df.to_csv(os.path.join(sys.path[0],(f'{self.target_column}_data_frame.csv')), index=False)
        else:
            self.df.to_csv(os.path.join(sys.path[0],(f'{self.target_column}_data_frame.csv')), index=False)
        return self.df
        
        

        
class temperatureDataFrame(SousDataFrame):
    def __init__(self,dataframe:DataFrame=None):
        self.target_column = 'temperature_2m_mean'
        if os.path.exists(os.path.join(sys.path[0], f"{self.target_column}_data_frame.csv")):
            self.dataframe = pd.read_csv(os.path.join(sys.path[0], f"{self.target_column}_data_frame.csv"))
        else:
            self.dataframe = None
        super().__init__(self.dataframe)
    
    def df_date(self):
        return super().df_date()
    
    def feature_engineering(self):
        df_temp=self.df_date().copy()
        for i in range (1,4):
            df_temp[f"temperature_moy_j-{i}"]=self.df['temperature_2m_mean'].shift(i)
        df_temp[f"precipitation_sum_j-1"]=self.df['precipitation_sum'].shift(1)

        df_temp['temperature_2m_mean'] = self.df['temperature_2m_mean'] 
        df_temp["wind_speed_10m_max_j-1"]=self.df['wind_speed_10m_max'].shift(1)
        df_temp['saison'] = self.df['mois'].apply(lambda x:
            1 if x in [12, 1, 2] else      
            2 if x in [3, 4, 5] else       
            3 if x in [6, 7, 8] else       
            4)
        return df_temp.dropna()
    def ajouter_une_ligne(self):
        self.feature_engineering()
        super().ajouter_une_ligne()
        
    def get_target_column(self):
        return 'temperature_2m_mean'
class precipitationDataFrame(SousDataFrame):
    def __init__(self,dataframe:DataFrame=None):
        self.target_column = 'precipitation_sum'
        if os.path.exists(os.path.join(sys.path[0], f"{self.target_column}_data_frame.csv")):
            self.dataframe=pd.read_csv(os.path.join(sys.path[0], f"{self.target_column}_data_frame.csv"))
        else:
            self.dataframe=None
        super().__init__(self.dataframe)
    
    def df_date(self):
        return super().df_date()
    
    def feature_engineering(self):
        df_precip = self.df_date().copy()
        for i in range(1, 4):
            df_precip[f"precipitation_sum_j-{i}"] = self.df['precipitation_sum'].shift(i)
        df_precip["temperature_2m_mean_j-1"] = self.df['temperature_2m_mean'].shift(1)
        df_precip["pressure_msl_mean_j-1"] = self.df['pressure_msl_mean'].shift(1)
        df_precip["cloud_cover_mean_j-1"] = self.df['cloud_cover_mean'].shift(1)
        df_precip['saison'] = self.df['mois'].apply(lambda x:
            1 if x in [12, 1, 2] else
            2 if x in [3, 4, 5] else
            3 if x in [6, 7, 8] else
            4)
        df_precip['precipitation_sum'] = self.df['precipitation_sum']
        
        return df_precip.dropna()
    def ajouter_une_ligne(self):
        self.feature_engineering()
        super().ajouter_une_ligne()
    def get_target_column(self):
        return 'precipitation_sum'
class WindSpeedDataFrame(SousDataFrame):
    def __init__(self, df=None):
        self.target_column = 'wind_speed_10m_max'
        if os.path.exists(os.path.join(sys.path[0], f"{self.target_column}_data_frame.csv")):
            self.df=pd.read_csv(os.path.join(sys.path[0], f"{self.target_column}_data_frame.csv"))
        else:
            self.df=None
        super().__init__(self.df)
        
    
    def feature_engineering(self):
        df_wind = self.df_date().copy()
        
        for i in range(1, 4):
            df_wind[f"wind_speed_10m_max_j-{i}"] = self.df['wind_speed_10m_max'].shift(i)
        
        df_wind["pressure_msl_mean_j-1"] = self.df['pressure_msl_mean'].shift(1)
        
        df_wind['saison'] = self.df['mois'].apply(lambda x:
            1 if x in [12, 1, 2] else
            2 if x in [3, 4, 5] else
            3 if x in [6, 7, 8] else
            4)
        
        df_wind['wind_speed_10m_max'] = self.df['wind_speed_10m_max']
        
        return df_wind.dropna()
    def get_target_column(self):
        return 'wind_speed_10m_max'
    def ajouter_une_ligne(self):
        self.feature_engineering()
        super().ajouter_une_ligne()


class PressureDataFrame(SousDataFrame):
    def __init__(self, df=None):
        self.target_column = 'pressure_msl_mean'
        if os.path.exists(os.path.join(sys.path[0], f"{self.target_column}_data_frame.csv")):
            self.df=pd.read_csv(os.path.join(sys.path[0], f"{self.target_column}_data_frame.csv"))
        else:
            self.df=None
        super().__init__(self.df)
        
    
    def feature_engineering(self):
        df_pressure = self.df_date().copy()
        
        for i in range(1, 4):
            df_pressure[f"pressure_msl_mean_j-{i}"] = self.df['pressure_msl_mean'].shift(i)
        
        df_pressure["temperature_2m_mean_j-1"] = self.df['temperature_2m_mean'].shift(1)
        
        df_pressure['saison'] = self.df['mois'].apply(lambda x:
            1 if x in [12, 1, 2] else
            2 if x in [3, 4, 5] else
            3 if x in [6, 7, 8] else
            4)
        
        df_pressure['pressure_msl_mean'] = self.df['pressure_msl_mean']
        
        return df_pressure.dropna()
    def get_target_column(self):
        return 'pressure_msl_mean'
    def ajouter_une_ligne(self):
        self.feature_engineering()
        super().ajouter_une_ligne()


class CloudCoverDataFrame(SousDataFrame):
    def __init__(self, df=None):
        self.target_column = 'cloud_cover_mean'
        if os.path.exists(os.path.join(sys.path[0], f"{self.target_column}_data_frame.csv")):
            self.df=pd.read_csv(os.path.join(sys.path[0], f"{self.target_column}_data_frame.csv"))
        else:
            self.df=None
        super().__init__(self.df)
        self.target_column = 'cloud_cover_mean'
    
    def feature_engineering(self):
        df_cloud = self.df_date().copy()
        
        for i in range(1, 4):
            df_cloud[f"cloud_cover_mean_j-{i}"] = self.df['cloud_cover_mean'].shift(i)
        
        df_cloud["precipitation_sum_j-1"] = self.df['precipitation_sum'].shift(1)
        
        df_cloud['saison'] = self.df['mois'].apply(lambda x:
            1 if x in [12, 1, 2] else
            2 if x in [3, 4, 5] else
            3 if x in [6, 7, 8] else
            4)
        
        df_cloud['cloud_cover_mean'] = self.df['cloud_cover_mean']
        
        return df_cloud.dropna()
    def get_target_column(self):
        return 'cloud_cover_mean'
    def ajouter_une_ligne(self):
        self.feature_engineering()
        super().ajouter_une_ligne()