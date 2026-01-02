from extract import archive,forecast
from sous_data_frame import (
    SousDataFrame,
    temperatureDataFrame,
    precipitationDataFrame,
    WindSpeedDataFrame,
    PressureDataFrame,
    CloudCoverDataFrame
)
from abc import ABC, abstractmethod
from prediction import Model
from train_split import train_split
class predictions(ABC):
    def __init__(self,df_processor: SousDataFrame,model:Model=None):
        self.df_processor=df_processor
        if model is None:

            self.model=Model()

            
    @abstractmethod
    def execute(self,y,colonne_name):
        df=self.df_processor
        train_instance=train_split(df)

        x_train, y_train, x_test, y_test = train_instance.split(colonne_name)
        self.model.train(df,x_train, y_train)
        predictions = self.model.predict(y)
        return predictions, y_test
class temperaturePrediction(predictions):
    def __init__(self,df_processor:temperatureDataFrame,model:Model=None):
        super().__init__(df_processor, model)
    def execute(self):
        return super().execute()
class precipitationPrediction(predictions):
    def __init__(self,df_processor:precipitationDataFrame,model:Model=None):
        super().__init__(df_processor, model)
    def execute(self):
        return super().execute()
class windSpeedPrediction(predictions):
    def __init__(self,df_processor:WindSpeedDataFrame,model:Model=None):
        super().__init__(df_processor, model)
    def execute(self):
        return super().execute()
class pressurePrediction(predictions):
    def __init__(self,df_processor:PressureDataFrame,model:Model=None):
        super().__init__(df_processor, model)
    def execute(self):
        return super().execute()
class cloudCoverPrediction(predictions):
    def __init__(self,df_processor:CloudCoverDataFrame,model:Model=None):
        super().__init__(df_processor, model)
    def execute(self):
        return super().execute()

    
    



