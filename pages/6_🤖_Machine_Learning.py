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
# CHECK DATA
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
# TRAIN TEST SPLIT
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# ==========================
# MODEL COMPARISON
# ==========================

st.subheader(
    "🏆 Compare Models"
)



if st.button(
    "🚀 Compare All Models"
):


    models = {

        "Linear Regression":
        LinearRegression(),

        "Decision Tree":
        DecisionTreeRegressor(
            random_state=42
        ),

        "Random Forest":
        RandomForestRegressor(
            random_state=42
        )

    }


    comparison_results = []


    for name, model_test in models.items():


        model_test.fit(
            X_train,
            y_train
        )


        prediction = model_test.predict(
            X_test
        )


        mae = mean_absolute_error(
            y_test,
            prediction
        )


        rmse = mean_squared_error(
            y_test,
            prediction
        ) ** 0.5


        r2 = r2_score(
            y_test,
            prediction
        )


        comparison_results.append(
            {
                "Model": name,
                "MAE": round(mae,3),
                "RMSE": round(rmse,3),
                "R² Score": round(r2,3)
            }
        )



    comparison = pd.DataFrame(
        comparison_results
    )


    st.dataframe(
        comparison,
        use_container_width=True
    )



    best = comparison.loc[
        comparison["R² Score"].idxmax()
    ]



    st.success(
        f"🏆 Best Model : {best['Model']} "
        f"(R² = {best['R² Score']})"
    )



# ==========================
# CHOOSE MODEL
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



    mae = mean_absolute_error(
        y_test,
        predictions
    )


    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.5


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
    # SAVE RESULTS
    # ==========================


    st.session_state["ml_results"] = {

        "model_name": model_name,

        "mae": mae,

        "rmse": rmse,

        "r2": r2,

        "features": features

    }



    st.success(
        "✅ Model trained and saved!"
    )



    # ==========================
    # METRICS
    # ==========================

    st.subheader(
        "📊 Model Performance"
    )


    c1,c2,c3,c4 = st.columns(4)



    c1.metric(
        "MAE",
        round(mae,3)
    )


    c2.metric(
        "RMSE",
        round(rmse,3)
    )


    c3.metric(
        "R² Score",
        round(r2,3)
    )


    c4.metric(
        "Samples",
        len(y_test)
    )



    # ==========================
    # GRAPH
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
                "Importance": model.feature_importances_
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
    # PREDICTIONS TABLE
    # ==========================

    st.subheader(
        "🔮 Predictions"
    )


    result = pd.DataFrame(
        {
            "Actual": y_test,
            "Prediction": predictions
        }
    )


    st.dataframe(
        result,
        use_container_width=True
    )