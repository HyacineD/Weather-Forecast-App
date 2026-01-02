import requests
from datetime import date, timedelta
from abc import ABC, abstractmethod
class Extract(ABC):
    def __init__ (self, latitude:str, longitude:str, params:dict=None, start_date='1990-12-31', end_date='1991-12-31') -> None:
        self.latitude = latitude
        self.longitude = longitude
        # Default: last 2 years of data
        if start_date is None:
            start_date = '1990-12-31'
        if end_date is None:
            end_date = '2013-12-10'
        self.start_date = start_date
        self.end_date = end_date
        from split_time import split_period
        self.periode= split_period(self.start_date, self.end_date, chunk_days=365)

        self.params = params
    @abstractmethod
    def fetch_data(self,*args):
        try:
            print(f"Fetching data from: {args[0]}")
            print(f"Parameters: {self.params}")
            
            response=requests.get(args[0], params=self.params, timeout=120)
            
            print(f"Response status code: {response.status_code}")
            
            response.raise_for_status()  # Raise exception for bad status codes
            data=response.json()
            
            # Check if 'daily' key exists in response
            if 'daily' not in data:
                error_msg = data.get('reason', data.get('error', 'Unknown error'))
                print(f"API response: {data}")
                raise ValueError(f"API returned error: {error_msg}")
            
            print(f"Data fetched successfully - {len(data['daily']['time'])} records")
            return data['daily']
            
        except requests.exceptions.Timeout:
            print(f"Error: Request timeout after 30 seconds")
            raise
        except requests.exceptions.ConnectionError as e:
            print(f"Error: Connection failed - {e}")
            raise
        except requests.exceptions.HTTPError as e:
            print(f"Error: HTTP error - {e}")
            print(f"Response content: {response.text[:500]}")
            raise
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            raise
        except ValueError as e:
            print(f"Error: Invalid response format - {e}")
            raise
        except Exception as e:
            print(f"Unexpected error: {type(e).__name__} - {e}")
            raise
class archive(Extract):
    url="https://archive-api.open-meteo.com/v1/archive"
    def __init__ (self, latitude:str, longitude:str, params=None, start_date=None, end_date=None,api_url:str=url) -> None:
        # Archive API only accepts historical data, so use yesterday as default end_date

            
        super().__init__(latitude, longitude, params, start_date, end_date)
        self.api_url=api_url
        self.params = {
        "latitude": self.latitude,
        "longitude": self.longitude,
        "start_date": self.start_date,
        "end_date": self.end_date,
        "daily": ",".join([
        "temperature_2m_max",
        "temperature_2m_min",
        "temperature_2m_mean",
        "precipitation_sum",
        "rain_sum",
        "snowfall_sum",
        "wind_speed_10m_max",
        "pressure_msl_mean",
        "cloud_cover_mean"
        ]),
        "timezone": "Africa/Algiers"
    }
    def fetch_data(self):
        for item in self.periode:
            self.params['start_date']=item[0]
            self.params['end_date']=item[1]
            from df_archive_to_csv import df_archive_to_csv
            df_archive_to_csv(item[0],item[1],super().fetch_data(self.api_url))
        
        return super().fetch_data(self.api_url)
class forecast(Extract):
    url="https://api.open-meteo.com/v1/forecast"
    def __init__ (self, latitude:str, longitude:str, params=None, start_date=None, end_date=None,api_url:str=url) -> None:
        super().__init__(latitude, longitude, params, start_date, end_date)
        self.api_url=api_url
        self.params = {
        "latitude": self.latitude,
        "longitude": self.longitude,
        "forecast_days":1,
        "past_days":60,
        "daily": ",".join([
        "temperature_2m_max",
        "temperature_2m_min",
        "temperature_2m_mean",
        "precipitation_sum",
        "rain_sum",
        "snowfall_sum",
        "wind_speed_10m_max",
        "pressure_msl_mean",
        "cloud_cover_mean"
        ]),
        "timezone": "Africa/Algiers"
    }
    def fetch_data(self):
        return super().fetch_data(self.api_url)