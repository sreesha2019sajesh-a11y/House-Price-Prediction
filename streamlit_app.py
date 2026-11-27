import streamlit as st
import joblib
import pandas as pd


# Load trained model
model = joblib.load("model.pkl")


# Application title
st.title("House Price Prediction System")


st.write(
    "Enter the house details to predict its price."
)


st.divider()


# User input
area = st.number_input(
    "House Area (sq. ft.)",
    min_value=100,
    max_value=10000,
    value=1500
)


bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)


age = st.number_input(
    "Age of House (Years)",
    min_value=0,
    max_value=100,
    value=5
)


# Prediction button
if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "age": [age]
    })

    prediction = model.predict(input_data)

    price = float(prediction[0])

    st.success(
        "Predicted House Price: ₹"
        + format(price, ",.2f")
    )

    # New in version 2: price per square foot
    st.info(
        "Price per sq. ft.: ₹"
        + format(price / area, ",.2f")
    )

    # New in version 2: summary of the inputs
    st.subheader("Input Summary")
    st.table(input_data)

