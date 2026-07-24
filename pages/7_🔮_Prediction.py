import streamlit as st
import joblib
import pandas as pd
import os



st.set_page_config(
    page_title="Prediction",
    page_icon="🔮",
    layout="wide"
)


st.title(
    "🔮 Prediction"
)



# ==========================
# CHECK MODEL
# ==========================

model_path = "models/model.pkl"



if not os.path.exists(model_path):

    st.warning(
        "⚠️ Please train a model first."
    )

    st.stop()



# Load model

saved_model = joblib.load(
    model_path
)


model = saved_model["model"]

features = saved_model["features"]



st.subheader(
    "Enter values"
)



input_data = {}



for feature in features:

    input_data[feature] = st.number_input(
        feature
    )



# Convert input

input_df = pd.DataFrame(
    [input_data]
)



# Prediction

if st.button(
    "🔮 Predict"
):


    prediction = model.predict(
        input_df
    )


    st.success(
        "Prediction completed!"
    )


    st.metric(
        "Predicted Value",
        round(
            prediction[0],
            2
        )
    )