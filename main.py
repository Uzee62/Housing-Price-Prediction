from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pickle
import json
import sklearn
from schemas import model_input


app = FastAPI()



#Load the saved model

Housing_price_pred = pickle.load(open("HousePricePrediction.pkl", "rb"))

# creating an  API
@app.post("/HousingPricePrediction")
def HousingPrice(input:model_input):
    input_data = input.json()
    input_dict = json.loads(input_data)
    
    longitude=  input_dict["longitude"]
    latitude= input_dict["latitude"]
    housing_median_age= input_dict["housing_median_age"]
    total_room= input_dict["total_rooms"]
    total_bedroom= input_dict["total_bedrooms"]
    population= input_dict["population"]
    household= input_dict["households"]
    median_income= input_dict["median_income"]
    ocean_proximity_INLANd= input_dict["ocean_proximity_INLAND"]
    ocean_proximity_ISLANd= input_dict["ocean_proximity_ISLAND"]
    ocean_proximity_NEAR_bay= input_dict["ocean_proximity_NEAR_bay"]
    ocean_proximity_Ocean= input_dict["ocean_proximity_Ocean"]
    
    
    input_list =[longitude,latitude,housing_median_age,total_room,total_bedroom,population,household,median_income,ocean_proximity_INLANd,ocean_proximity_ISLANd,ocean_proximity_NEAR_bay,ocean_proximity_Ocean]
    
    
    prediction = Housing_price_pred.predict([input_list])
    return {"prediction": prediction.tolist()}