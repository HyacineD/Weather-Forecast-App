from fastapi import FastAPI
import pandas as pd
import json
from fastapi.middleware.cors import CORSMiddleware
from config import PORT, HOST
df=pd.read_csv('predictions_6_jours.csv')
dict_records=df.to_dict(orient='records')
print(dict_records)
app = FastAPI()
@app.get("/predictions/")
def get_predictions():
    return json.dumps(dict_records)
origins = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     
    allow_credentials=True,
    allow_methods=["*"],      
    allow_headers=["*"],
)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)
