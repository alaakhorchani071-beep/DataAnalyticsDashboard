import streamlit as st
import pandas as pd


# ==========================
# CONFIGURATION
# ==========================

st.set_page_config(
    page_title="Dashboard - Data Analytics",
    page_icon="📊",
    layout="wide"
)


st.title(
    "📊 Data Analytics Dashboard"
)



# ==========================
# INTRODUCTION
# ==========================

st.write(
"""
Welcome to the Data Analytics Dashboard 🚀

This application allows you to:

✅ Import and clean datasets  
✅ Analyze data statistically  
✅ Create visualizations  
✅ Train Machine Learning models  
✅ Generate professional PDF reports
"""
)



st.divider()



# ==========================
# CHECK DATA
# ==========================

if "data" not in st.session_state:


    st.info(
        "📂 Please upload a dataset to display dashboard information."
    )


    st.stop()



data = st.session_state["data"]



# ==========================
# DATASET KPI
# ==========================

st.subheader(
    "📌 Dataset Overview"
)



rows = data.shape[0]

columns = data.shape[1]

missing = data.isnull().sum().sum()

duplicates = data.duplicated().sum()



col1, col2, col3, col4 = st.columns(4)



col1.metric(
    "Rows",
    rows
)


col2.metric(
    "Columns",
    columns
)


col3.metric(
    "Missing Values",
    missing
)


col4.metric(
    "Duplicates",
    duplicates
)



st.divider()



# ==========================
# DATA PREVIEW
# ==========================

st.subheader(
    "👀 Data Preview"
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
    "📋 Column Information"
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
    "💡 Data Insights"
)


numeric_columns = data.select_dtypes(
    include=["number"]
).columns


text_columns = data.select_dtypes(
    include=["object"]
).columns



col1, col2, col3, col4 = st.columns(4)



col1.metric(
    "🔢 Numeric Columns",
    len(numeric_columns)
)


col2.metric(
    "🔤 Text Columns",
    len(text_columns)
)


col3.metric(
    "💾 Dataset Size",
    f"{round(data.memory_usage().sum()/1024,2)} KB"
)


missing_column = (
    data.isnull()
    .sum()
    .idxmax()
)


col4.metric(
    "⚠️ Most Missing",
    missing_column
)
# ==========================
# AUTOMATIC CHART
# ==========================

st.subheader(
    "📈 Automatic Visualization"
)


numeric = data.select_dtypes(
    include=["number"]
)


if len(numeric.columns) > 0:

    selected = st.selectbox(
        "Choose numerical column",
        numeric.columns
    )


    st.line_chart(
        numeric[selected]
    )

else:

    st.info(
        "No numerical columns available."
    )
# ==========================
# MACHINE LEARNING SUMMARY
# ==========================

st.subheader(
    "🤖 Machine Learning Summary"
)



if "ml_results" in st.session_state:


    ml = st.session_state["ml_results"]


    c1, c2, c3 = st.columns(3)


    c1.metric(
        "Model",
        ml["model_name"]
    )


    c2.metric(
        "R² Score",
        round(
            ml["r2"],
            3
        )
    )


    c3.metric(
        "RMSE",
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
    "👩‍💻 Developer"
)


st.write(
"""
Developed by:

**Alaa Khorchani**

Mathematics Applied - Data Science
"""
)