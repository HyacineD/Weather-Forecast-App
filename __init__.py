from run import *
from sous_data_frame import *
from train_split import train_split
from x_test import XTestBuilder
from prediction import Model
from datetime import datetime, timedelta
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os
import sys

def main():
    try:
        print("=== Démarrage du système de prédiction météo ===\n")
        
        df_original_path = os.path.join(sys.path[0], 'data_weather_full.csv')
        if not os.path.exists(df_original_path):
            print("Erreur: data_weather_full.csv n'existe pas. Création des données")
            temp_df = temperatureDataFrame()
            df_original = pd.read_csv(df_original_path)
        else:
            df_original = pd.read_csv(df_original_path)
        df_original['date'] = pd.to_datetime(df_original['date'])
        print(f"✓ DataFrame original chargé: {len(df_original)} lignes")
        print(f"  Dernière date: {df_original['date'].max()}\n")
        print("=== Création des SousDataFrame ===")
        dataframe_wrapper = DataFrame(forecast(latitude="36.7538", longitude="3.0588").fetch_data())
        
        dataframes_ordered = [
            ("pressure", PressureDataFrame(dataframe_wrapper), "pressure_msl_mean"),
            ("wind_speed", WindSpeedDataFrame(dataframe_wrapper), "wind_speed_10m_max"),
            ("temperature", temperatureDataFrame(dataframe_wrapper), "temperature_2m_mean"),
            ("cloud_cover", CloudCoverDataFrame(dataframe_wrapper), "cloud_cover_mean"),
            ("precipitation", precipitationDataFrame(dataframe_wrapper), "precipitation_sum")
        ]
        print("✓ SousDataFrame créés\n")

        print("=== Entraînement des modèles ===")
        splitter = train_split(df_original)
        models = {}
        
        for name, sous_df, target_col in dataframes_ordered:
            print(f"Entraînement du modèle: {name}...")
            x_train, y_train, x_test, y_test = splitter.split(sous_df)
            
            model = Model()
            model.train(df_original, x_train, y_train)
            models[target_col] = model
            
            # Évaluation sur le test set
            predictions = model.predict(x_test)
            mae = mean_absolute_error(y_test, predictions)
            mse = mean_squared_error(y_test, predictions)
            r2 = r2_score(y_test, predictions)
            
            print(f"  ✓ {name}: MAE={mae:.2f}, MSE={mse:.2f}, R²={r2:.3f}")
        
        print("\n=== Prédictions pour les 6 prochains jours ===\n")
        derniere_date = df_original['date'].max()
        all_predictions = []
        
        for day in range(1, 7):
            date_to_predict = derniere_date + timedelta(days=day)
            print(f"--- Prédiction pour {date_to_predict.strftime('%Y-%m-%d')} (j+{day}) ---")
            
            predictions_temp = {}

            for name, sous_df, target_col in dataframes_ordered:
                x_test = splitter.create_x_test_for_prediction(
                    target_col, 
                    date_to_predict, 
                    predictions_temp
                )
                prediction = models[target_col].predict(x_test)
                predictions_temp[target_col] = prediction[0]
                
                print(f"  {name}: {prediction[0]:.2f}")
            all_predictions.append({
                'date': date_to_predict,
                'jour': date_to_predict.day,
                'mois': date_to_predict.month,
                'annee': date_to_predict.year,
                'pressure_msl_mean': predictions_temp['pressure_msl_mean'],
                'wind_speed_10m_max': predictions_temp['wind_speed_10m_max'],
                'temperature_2m_mean': predictions_temp['temperature_2m_mean'],
                'cloud_cover_mean': predictions_temp['cloud_cover_mean'],
                'precipitation_sum': predictions_temp['precipitation_sum']
            })

            new_row = pd.DataFrame([{
                'date': date_to_predict,
                'jour': date_to_predict.day,
                'mois': date_to_predict.month,
                'annee': date_to_predict.year,
                'pressure_msl_mean': predictions_temp['pressure_msl_mean'],
                'wind_speed_10m_max': predictions_temp['wind_speed_10m_max'],
                'temperature_2m_mean': predictions_temp['temperature_2m_mean'],
                'cloud_cover_mean': predictions_temp['cloud_cover_mean'],
                'precipitation_sum': predictions_temp['precipitation_sum'],
                'temperature_2m_max': None,
                'temperature_2m_min': None,
                'rain_sum': None,
                'snowfall_sum': None
            }])
            
            df_original = pd.concat([df_original, new_row], ignore_index=True)
            print()
        print("=== Sauvegarde des prédictions ===")
        predictions_df = pd.DataFrame(all_predictions)
        predictions_path = os.path.join(sys.path[0], 'predictions_6_jours.csv')
        predictions_df.to_csv(predictions_path, index=False)
        print(f"✓ Prédictions sauvegardées dans: {predictions_path}")
        df_original.to_csv(df_original_path, index=False)
        print(f"✓ DataFrame original mis à jour: {df_original_path}")
        
        print("\n=== Résumé des prédictions ===")
        print(predictions_df.to_string(index=False))
        
        print("\n✓ Prédictions terminées avec succès!")
        
    except Exception as e:
        print(f" Erreur: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
    from api import run
    run()
