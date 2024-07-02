from pydantic import BaseModel

class model_input(BaseModel):
    longitude                 :float
    latitude                  :float
    housing_median_age        :float
    total_rooms               :float
    total_bedrooms            :float
    population                :float
    households                :float
    median_income             :float
    ocean_proximity_INLAND    :float
    ocean_proximity_ISLAND    :float    
    ocean_proximity_NEAR_bay  :float
    ocean_proximity_Ocean     :float