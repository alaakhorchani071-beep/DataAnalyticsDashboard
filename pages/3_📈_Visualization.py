import streamlit as st
import plotly.express as px
from translations import translations
from src.logo import show_logo



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
    page_title="Visualization",
    page_icon="📈",
    layout="wide"
)
show_logo()
st.title(
    t["visualization"]
)



# ==========================
# CHECK DATA
# ==========================

if "data" not in st.session_state:


    st.warning(
        "⚠️ " + t["upload_first"]
    )


    st.stop()



data = st.session_state["data"]



# ==========================
# SELECT COLUMN
# ==========================

st.subheader(
    t["choose_column"]
)



column = st.selectbox(
    t["choose_column"],
    data.columns
)



# ==========================
# CHART TYPE
# ==========================

chart_type = st.selectbox(

    t["chart_type"],

    [
        t["histogram"],
        t["bar"],
        t["line"],
        t["pie"]
    ]

)



# ==========================
# GRAPHIQUES
# ==========================


if chart_type == t["histogram"]:


    fig = px.histogram(

        data,

        x=column,

        title=f"{t['histogram']} - {column}"

    )



elif chart_type == t["bar"]:


    values = (
        data[column]
        .value_counts()
        .reset_index()
    )



    values.columns = [

        column,

        "Count"

    ]



    fig = px.bar(

        values,

        x=column,

        y="Count",

        title=f"{t['bar']} - {column}"

    )



elif chart_type == t["line"]:


    fig = px.line(

        data,

        y=column,

        title=f"{t['line']} - {column}"

    )



else:


    values = (

        data[column]

        .value_counts()

        .reset_index()

    )



    values.columns = [

        column,

        "Count"

    ]



    fig = px.pie(

        values,

        names=column,

        values="Count",

        title=f"{t['pie']} - {column}"

    )



# ==========================
# DISPLAY CHART
# ==========================

st.plotly_chart(

    fig,

    use_container_width=True

)