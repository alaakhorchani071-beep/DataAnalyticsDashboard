import streamlit as st
import plotly.express as px


st.set_page_config(
    page_title="Visualization",
    page_icon="📈",
    layout="wide"
)


st.title("📈 Data Visualization")


# Vérifier les données

if "data" not in st.session_state:

    st.warning(
        "⚠️ Please upload a file first."
    )

    st.stop()



data = st.session_state["data"]



st.subheader("Choose a column")


column = st.selectbox(
    "Column",
    data.columns
)



chart_type = st.selectbox(
    "Chart type",
    [
        "Histogram",
        "Bar chart",
        "Line chart",
        "Pie chart"
    ]
)



# ==========================
# Graphiques
# ==========================


if chart_type == "Histogram":


    fig = px.histogram(
        data,
        x=column,
        title=f"Distribution of {column}"
    )



elif chart_type == "Bar chart":


    values = data[column].value_counts().reset_index()


    values.columns = [
        column,
        "Count"
    ]


    fig = px.bar(
        values,
        x=column,
        y="Count",
        title=f"Bar chart of {column}"
    )



elif chart_type == "Line chart":


    fig = px.line(
        data,
        y=column,
        title=f"Evolution of {column}"
    )



else:


    values = data[column].value_counts().reset_index()


    values.columns = [
        column,
        "Count"
    ]


    fig = px.pie(
        values,
        names=column,
        values="Count",
        title=f"Distribution of {column}"
    )



st.plotly_chart(
    fig,
    use_container_width=True
)
