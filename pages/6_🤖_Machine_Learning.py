import os
import joblib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)



# ==========================
# CONFIGURATION
# ==========================

st.set_page_config(
    page_title="Machine Learning",
    page_icon="🤖",
    layout="wide"
)


st.title(
    "🤖 Machine Learning"
)



# ==========================
# VERIFICATION DATA
# ==========================

if "data" not in st.session_state:

    st.info(
        "📂 Please upload data first."
    )

    st.stop()



data = st.session_state["data"]



# ==========================
# NUMERIC COLUMNS
# ==========================

numeric_columns = data.select_dtypes(
    include="number"
).columns



if len(numeric_columns) < 2:

    st.error(
        "❌ Need at least two numeric columns."
    )

    st.stop()



# ==========================
# SELECT DATA
# ==========================

st.subheader(
    "⚙️ Select Data"
)


target = st.selectbox(
    "🎯 Target column",
    numeric_columns
)



features = st.multiselect(
    "📌 Feature columns",
    [
        col for col in numeric_columns
        if col != target
    ]
)



if len(features) == 0:

    st.warning(
        "Please select features."
    )

    st.stop()



X = data[features]

y = data[target]



# ==========================
# SELECT MODEL
# ==========================

st.subheader(
    "🧠 Choose Model"
)



model_name = st.selectbox(
    "Model",
    [
        "Linear Regression",
        "Decision Tree",
        "Random Forest"
    ]
)



if model_name == "Linear Regression":

    model = LinearRegression()


elif model_name == "Decision Tree":

    model = DecisionTreeRegressor(
        random_state=42
    )


else:

    model = RandomForestRegressor(
        random_state=42
    )



# ==========================
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# ==========================
# TRAIN MODEL
# ==========================

if st.button(
    "🚀 Train Model"
):


    model.fit(
        X_train,
        y_train
    )


    predictions = model.predict(
        X_test
    )



    # ==========================
    # METRICS
    # ==========================

    mae = mean_absolute_error(
        y_test,
        predictions
    )


    mse = mean_squared_error(
        y_test,
        predictions
    )


    rmse = mse ** 0.5


    r2 = r2_score(
        y_test,
        predictions
    )



    # ==========================
    # SAVE MODEL
    # ==========================

    if not os.path.exists(
        "models"
    ):

        os.makedirs(
            "models"
        )



    model_data = {

        "model": model,

        "features": features,

        "target": target,

        "model_name": model_name

    }



    joblib.dump(
        model_data,
        "models/model.pkl"
    )



    # ==========================
    # SAVE ML RESULTS
    # FOR PDF REPORT
    # ==========================

    st.session_state["ml_results"] = {

        "model_name": model_name,

        "mae": mae,

        "rmse": rmse,

        "r2": r2,

        "features": features

    }



    st.success(
        "✅ Model trained and saved successfully!"
    )



    # ==========================
    # PERFORMANCE
    # ==========================

    st.subheader(
        "📊 Model Performance"
    )


    c1, c2, c3, c4 = st.columns(4)



    c1.metric(
        "MAE",
        round(mae, 3)
    )


    c2.metric(
        "RMSE",
        round(rmse, 3)
    )


    c3.metric(
        "R² Score",
        round(r2, 3)
    )


    c4.metric(
        "Samples",
        len(y_test)
    )



    # ==========================
    # ACTUAL VS PREDICTION
    # ==========================

    st.subheader(
        "📈 Actual vs Prediction"
    )


    fig, ax = plt.subplots()


    ax.scatter(
        y_test,
        predictions
    )


    ax.set_xlabel(
        "Actual Values"
    )


    ax.set_ylabel(
        "Predicted Values"
    )


    ax.set_title(
        "Actual vs Predicted"
    )


    st.pyplot(fig)



    # ==========================
    # FEATURE IMPORTANCE
    # ==========================

    if model_name in [
        "Decision Tree",
        "Random Forest"
    ]:


        st.subheader(
            "🌳 Feature Importance"
        )


        importance = pd.DataFrame(
            {
                "Feature": features,

                "Importance":
                model.feature_importances_
            }
        )


        importance = importance.sort_values(
            by="Importance",
            ascending=False
        )


        st.bar_chart(
            importance.set_index(
                "Feature"
            )
        )



    # ==========================
    # PREDICTION TABLE
    # ==========================

    st.subheader(
        "🔮 Predictions"
    )


    results = pd.DataFrame(
        {
            "Actual": y_test,

            "Prediction": predictions
        }
    )


    st.dataframe(
        results,
        use_container_width=True
    )