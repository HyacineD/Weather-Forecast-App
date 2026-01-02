import pandas as pd
from datetime import timedelta

class XTestBuilder:
    def __init__(self, df_original: pd.DataFrame, date_to_predict, predictions_temp=None):

        self.df_original = df_original
        self.date = date_to_predict
        self.predictions_temp = predictions_temp or {}
    
    def _get_value(self, variable, days_back):

        target_date = self.date - timedelta(days=days_back)
        
        if variable in self.predictions_temp:
            return self.predictions_temp[variable]
        try:
            row = self.df_original[self.df_original['date'] == target_date]
            if not row.empty:
                return row.iloc[0][variable]
        except:
            pass
        
        return None
    
    def _get_saison(self):
        mois = self.date.month
        if mois in [12, 1, 2]:
            return 1
        elif mois in [3, 4, 5]:
            return 2
        elif mois in [6, 7, 8]:
            return 3
        else:
            return 4
    
    def build_x_test_pressure(self):

        x_test = pd.DataFrame({
            'date': [self.date],
            'jour': [self.date.day],
            'mois': [self.date.month],
            'annee': [self.date.year],
            'pressure_msl_mean_j-1': [self._get_value('pressure_msl_mean', 1)],
            'pressure_msl_mean_j-2': [self._get_value('pressure_msl_mean', 2)],
            'pressure_msl_mean_j-3': [self._get_value('pressure_msl_mean', 3)],
            'temperature_2m_mean_j-1': [self._get_value('temperature_2m_mean', 1)],
            'saison': [self._get_saison()]
        })
        return x_test
    
    def build_x_test_wind(self):
        x_test = pd.DataFrame({
            'date': [self.date],
            'jour': [self.date.day],
            'mois': [self.date.month],
            'annee': [self.date.year],
            'wind_speed_10m_max_j-1': [self._get_value('wind_speed_10m_max', 1)],
            'wind_speed_10m_max_j-2': [self._get_value('wind_speed_10m_max', 2)],
            'wind_speed_10m_max_j-3': [self._get_value('wind_speed_10m_max', 3)],
            'pressure_msl_mean_j-1': [self._get_value('pressure_msl_mean', 1)],
            'saison': [self._get_saison()]
        })
        return x_test
    
    def build_x_test_temperature(self):

        x_test = pd.DataFrame({
            'date': [self.date],
            'jour': [self.date.day],
            'mois': [self.date.month],
            'annee': [self.date.year],
            'temperature_moy_j-1': [self._get_value('temperature_2m_mean', 1)],
            'temperature_moy_j-2': [self._get_value('temperature_2m_mean', 2)],
            'temperature_moy_j-3': [self._get_value('temperature_2m_mean', 3)],
            'precipitation_sum_j-1': [self._get_value('precipitation_sum', 1)],
            'wind_speed_10m_max_j-1': [self._get_value('wind_speed_10m_max', 1)],
            'saison': [self._get_saison()]
        })
        return x_test
    
    def build_x_test_cloud(self):
        x_test = pd.DataFrame({
            'date': [self.date],
            'jour': [self.date.day],
            'mois': [self.date.month],
            'annee': [self.date.year],
            'cloud_cover_mean_j-1': [self._get_value('cloud_cover_mean', 1)],
            'cloud_cover_mean_j-2': [self._get_value('cloud_cover_mean', 2)],
            'cloud_cover_mean_j-3': [self._get_value('cloud_cover_mean', 3)],
            'precipitation_sum_j-1': [self._get_value('precipitation_sum', 1)],
            'saison': [self._get_saison()]
        })
        return x_test
    
    def build_x_test_precipitation(self):
        x_test = pd.DataFrame({
            'date': [self.date],
            'jour': [self.date.day],
            'mois': [self.date.month],
            'annee': [self.date.year],
            'precipitation_sum_j-1': [self._get_value('precipitation_sum', 1)],
            'precipitation_sum_j-2': [self._get_value('precipitation_sum', 2)],
            'precipitation_sum_j-3': [self._get_value('precipitation_sum', 3)],
            'temperature_2m_mean_j-1': [self._get_value('temperature_2m_mean', 1)],
            'pressure_msl_mean_j-1': [self._get_value('pressure_msl_mean', 1)],
            'cloud_cover_mean_j-1': [self._get_value('cloud_cover_mean', 1)],
            'saison': [self._get_saison()]
        })
        return x_test