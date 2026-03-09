import streamlit as st
import pandas as pd
import joblib as jb

model = jb.load("data/best_forest_model.pkl")
scaler = jb.load("data/scaler.pkl")

prediction = 150
choices = pd.read_csv("data/housing.csv")

def show_prediction_page():
    st.title("Californian houses price prediction")
    st.write("Please select your house features")


    longitude = st.number_input("Longitude", min_value=-125.0, max_value=125.0, value=0.0, step=0.1)

    latitude = st.number_input("Latitude", min_value=-125.0, max_value=125.0, value=0.0, step=0.1)

    housing_median_age = st.number_input("Housing Median Age", min_value=-125.0, value=0.0, step=0.1)

    total_rooms = st.number_input("Total rooms", min_value=0, value=0, step=1)

    total_bedrooms = st.number_input("Total bedrooms", min_value=0, value=0, step=1)

    population = st.number_input("Population", min_value=0.0, value=0.0, step=0.1)

    households = st.number_input("Households", min_value=0.0, value=0.0, step=0.1)

    ocean_proximity = st.selectbox("Ocean Proximity", choices["ocean_proximity"].unique())
    

    launch_prediction = st.button ("Predict" )

    if launch_prediction:

        data = {
            "longitude": longitude,
            "housing_median_age": housing_median_age,   
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "latitude": latitude,
            "households": households,
            "ocean_proximity": ocean_proximity,
        }

        data_df = pd.DataFrame([data])

        data_df["bedroom_ratio"] = data_df["total_bedrooms"] / data_df["total_rooms"]
        data_df["household_ratio"] = data_df["total_rooms"] / data_df["households"]

        data_df.join(pd.get_dummies(data_df["ocean_proximity"], dtype=int)).drop("ocean_proximity", axis=1)

        data_df_s = scaler.transform(data_df)

        prediction = model.predict(data_df_s)

        st.title(f"The estimated price is ${prediction[0]:.2f}")


