import streamlit as st
import pandas as pd
from translations import translations
from PIL import Image
import os

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
    page_title="Dashboard - Data Analytics",
    page_icon="📊",
    layout="wide"
)
# ==========================
# LOAD LOGO
# ==========================

logo_path = "logo.png.png"

if os.path.exists(logo_path):

    logo = Image.open(logo_path)

else:

    logo = None
# ==========================
# LOGO CENTER
# ==========================

if logo is not None:

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.image(
            logo,
            width=200
        )
st.title(
    t["title"]
)
# ==========================
# INTRODUCTION
# ==========================

st.write(
    t["description"]
)



st.divider()



# ==========================
# CHECK DATA
# ==========================

if "data" not in st.session_state:


    st.info(
        t["upload_first"]
    )


    st.stop()



data = st.session_state["data"]



# ==========================
# DATASET KPI
# ==========================

st.subheader(
    t["dataset_overview"]
)



rows = data.shape[0]

columns = data.shape[1]

missing = data.isnull().sum().sum()

duplicates = data.duplicated().sum()



col1, col2, col3, col4 = st.columns(4)



col1.metric(
    t["rows"],
    rows
)


col2.metric(
    t["columns"],
    columns
)


col3.metric(
    t["missing"],
    missing
)


col4.metric(
    t["duplicates"],
    duplicates
)



st.divider()



# ==========================
# DATA PREVIEW
# ==========================

st.subheader(
    t["data_preview"]
)



st.dataframe(
    data.head(),
    use_container_width=True
)



st.divider()



# ==========================
# COLUMN INFORMATION
# ==========================

st.subheader(
    t["column_information"]
)



info = pd.DataFrame(
    {
        "Column": data.columns,
        "Type": data.dtypes.astype(str),
        "Missing Values":
        data.isnull().sum()
    }
)



st.dataframe(
    info,
    use_container_width=True
)



st.divider()



# ==========================
# DATA INSIGHTS
# ==========================

st.subheader(
    t["data_insights"]
)



numeric_columns = data.select_dtypes(
    include=["number"]
).columns



text_columns = data.select_dtypes(
    include=["object"]
).columns



col1, col2, col3, col4 = st.columns(4)



col1.metric(
    t["numeric_columns"],
    len(numeric_columns)
)



col2.metric(
    t["text_columns"],
    len(text_columns)
)



col3.metric(
    t["dataset_size"],
    f"{round(data.memory_usage().sum()/1024,2)} KB"
)



missing_column = (
    data.isnull()
    .sum()
    .idxmax()
)



col4.metric(
    t["most_missing"],
    missing_column
)



# ==========================
# AUTOMATIC CHART
# ==========================

st.subheader(
    t["automatic_visualization"]
)



numeric = data.select_dtypes(
    include=["number"]
)



if len(numeric.columns) > 0:


    selected = st.selectbox(
        t["choose_column"],
        numeric.columns
    )


    st.line_chart(
        numeric[selected]
    )



else:


    st.info(
        t["no_numeric"]
    )



# ==========================
# MACHINE LEARNING SUMMARY
# ==========================

st.subheader(
    "🤖 Machine Learning"
)



if "ml_results" in st.session_state:


    ml = st.session_state["ml_results"]



    c1, c2, c3 = st.columns(3)



    c1.metric(
        "Model",
        ml["model_name"]
    )



    c2.metric(
        t["r2"],
        round(
            ml["r2"],
            3
        )
    )



    c3.metric(
        t["rmse"],
        round(
            ml["rmse"],
            3
        )
    )



else:


    st.info(
        "ℹ️ No trained model available yet."
    )



st.divider()



# ==========================
# DEVELOPER
# ==========================

st.subheader(
    f"👩‍💻 {t['developer']}"
)



st.write(
"""
**Alaa Khorchani**

Mathematics Applied - Data Science
"""
)