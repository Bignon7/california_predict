import streamlit as st
import pandas as pd
import joblib as jb

model = jb.load("model/best_forest_model.pkl")
scaler = jb.load("model/scaler.pkl")

prediction = 150
choices = pd.read_csv("data/housing.csv")

def show_prediction_page():
    st.title("Californian houses price prediction")
    st.write("Please select your house features")

    col1, col2 = st.columns(2)

    with col1:
        longitude = st.number_input("Longitude", min_value=-125.0, max_value=125.0, value=0.0, step=0.1)
        housing_median_age = st.number_input("Housing Median Age", min_value=0.0, value=0.0, step=0.1)
        total_rooms = st.number_input("Total rooms", min_value=0, value=0, step=1)
        population = st.number_input("Population", min_value=0.0, value=0.0, step=0.1)
        median_income = st.number_input("Median income", min_value=0.0, value=0.0, step=0.1)

    with col2:
        latitude = st.number_input("Latitude", min_value=-125.0, max_value=125.0, value=0.0, step=0.1)
        total_bedrooms = st.number_input("Total bedrooms", min_value=0, value=0, step=1)
        households = st.number_input("Households", min_value=0.0, value=0.0, step=0.1)
        ocean_proximity = st.selectbox("Ocean Proximity", choices["ocean_proximity"].unique())


    launch_prediction = st.button ("Predict" )

    if launch_prediction:

        data = {
            "longitude": longitude,
            "median_income": median_income,
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

        data_df = data_df.join(pd.get_dummies(data_df["ocean_proximity"], dtype=int)).drop("ocean_proximity", axis=1)
        
        #J'ai ajouté cette ligne pour refaire les colonnes de mon data_df en fonctions des colonnes de mon scaler, avec feature_names_in_
        data_df = data_df.reindex(columns=scaler.feature_names_in_, fill_value=0)

        data_df_s = scaler.transform(data_df)

        prediction = model.predict(data_df_s)

        st.title(f"The estimated price is ${prediction[0]:.2f}")


