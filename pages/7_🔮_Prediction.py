import streamlit as st
import joblib
import pandas as pd
import os

from src.logo import show_logo
from translations import translations



# ==========================
# LANGUAGE SYSTEM
# ==========================

language = st.session_state.get(
    "language",
    "Français"
)

t = translations[language]



# ==========================
# CONFIGURATION
# ==========================

st.set_page_config(
    page_title="Prediction",
    page_icon="🔮",
    layout="wide"
)


# LOGO

show_logo()



# ==========================
# TITLE
# ==========================

st.title(
    t.get(
        "prediction",
        "🔮 Prediction"
    )
)



# ==========================
# CHECK MODEL
# ==========================

model_path = "models/model.pkl"



if not os.path.exists(model_path):

    st.warning(
        t.get(
            "train_first",
            "⚠️ Please train a model first."
        )
    )

    st.stop()



# ==========================
# LOAD MODEL
# ==========================

saved_model = joblib.load(
    model_path
)



model = saved_model["model"]

features = saved_model["features"]



# ==========================
# INPUT VALUES
# ==========================

st.subheader(
    t.get(
        "enter_values",
        "✏️ Enter values"
    )
)



input_data = {}



for feature in features:

    input_data[feature] = st.number_input(
        feature,
        value=0.0
    )



# ==========================
# CONVERT DATA
# ==========================

input_df = pd.DataFrame(
    [input_data]
)



# ==========================
# PREDICTION
# ==========================

if st.button(
    t.get(
        "predict",
        "🔮 Predict"
    )
):


    prediction = model.predict(
        input_df
    )



    st.success(
        t.get(
            "prediction_success",
            "✅ Prediction completed successfully"
        )
    )



    st.metric(

        t.get(
            "prediction_result",
            "Prediction Result"
        ),

        round(
            prediction[0],
            2
        )

    )