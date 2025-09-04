from joblib import load
import pandas as pd
import numpy as np

# Loading the trained model
model = load("Dibrugarh_house_predictions.joblib")

# Example input: one house
input_data = {
    "area_sqft": [5000],
    "bedrooms": [9],
    "bathrooms": [11],
    "house_age_years": [30],
    "year_built": [1990],
    "floor_number": [2],
    "parking_spaces": [2],
    "has_garden": [2],
    "locality": ["Dibrugarh Town"],
    "building_type": ["Apartment"]
}

# input_data = {
#     "area_sqft": [int(input("Enter the area in sqft: "))],
#     "bedrooms": [int(input("Enter the number of bedrooms: "))],
#     "bathrooms": [int(input("Enter the number of bathrooms: "))],
#     "house_age_years": [int(input("Enter the age of the house (in years): "))],
#     "year_built": [int(input("Enter the year the house was built: "))],
#     "floor_number": [int(input("Enter the floor number: "))],
#     "parking_spaces": [int(input("Enter the number of parking spaces: "))],
#     "has_garden": [int(input("How many gardens (0 or 1): "))],
#     "locality": [input("Enter your locality: ")],
#     "building_type": [input("Enter your building type: ")]
# }


# Convert to DataFrame
input_df = pd.DataFrame(input_data)

# Predict (log scale)
predict_in_log = model.predict(input_df)

# Convert log price to INR
price_inr = np.expm1(predict_in_log)

print(f"house predicted price is: ₹{price_inr[0]:,.2f}")
