import streamlit as st

from src.analysis import (
    get_basic_info,
    get_statistics
)


st.set_page_config(
    page_title="Analysis",
    page_icon="📊",
    layout="wide"
)


st.title(
    "📊 Data Analysis"
)


# Vérifier si un fichier existe

if "data" not in st.session_state:

    st.warning(
        "⚠️ Please upload a file first from the Upload page."
    )

    st.stop()



data = st.session_state["data"]



# ==========================
# Informations générales
# ==========================

st.subheader(
    "📌 General Information"
)


info = get_basic_info(data)



col1, col2, col3, col4 = st.columns(4)



with col1:

    st.metric(
        "📄 Rows",
        info["Nombre de lignes"]
    )


with col2:

    st.metric(
        "📋 Columns",
        info["Nombre de colonnes"]
    )


with col3:

    st.metric(
        "❗ Missing values",
        info["Valeurs manquantes"]
    )


with col4:

    st.metric(
        "🔁 Duplicates",
        info["Doublons"]
    )



st.divider()



# ==========================
# Statistiques
# ==========================

st.subheader(
    "📈 Descriptive Statistics"
)



statistics = get_statistics(data)



st.dataframe(
    statistics,
    use_container_width=True
)
