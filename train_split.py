import pandas as pd
from sous_data_frame import SousDataFrame
from x_test import XTestBuilder  

class train_split:
    def __init__(self, df: pd.DataFrame, date_split=pd.Timestamp('2013-01-01')):

        self.df = df
        self.date_split = date_split
    
    def split(self, sous_df: SousDataFrame):
        df_with_features = sous_df.feature_engineering()
        target_column = sous_df.get_target_column()
        
        if not pd.api.types.is_datetime64_any_dtype(df_with_features['date']):
            df_with_features['date'] = pd.to_datetime(df_with_features['date'])
        

        x_train = df_with_features[df_with_features['date'] < self.date_split]
        x_train = x_train.drop(columns=[target_column])
        
        y_train = df_with_features[df_with_features['date'] < self.date_split][target_column]
        
        x_test = df_with_features[df_with_features['date'] >= self.date_split]
        x_test = x_test.drop(columns=[target_column])
        
        y_test = df_with_features[df_with_features['date'] >= self.date_split][target_column]
        
        return x_train, y_train, x_test, y_test
    
    def create_x_test_for_prediction(self, target_column: str, date_to_predict, predictions_temp=None):

        builder = XTestBuilder(self.df, date_to_predict, predictions_temp)

        if target_column == 'pressure_msl_mean':
            return builder.build_x_test_pressure()
        elif target_column == 'wind_speed_10m_max':
            return builder.build_x_test_wind()
        elif target_column == 'temperature_2m_mean':
            return builder.build_x_test_temperature()
        elif target_column == 'cloud_cover_mean':
            return builder.build_x_test_cloud()
        elif target_column == 'precipitation_sum':
            return builder.build_x_test_precipitation()
        else:
            raise ValueError(f"Target column inconnu: {target_column}")