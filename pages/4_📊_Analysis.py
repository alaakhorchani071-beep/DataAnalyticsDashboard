import streamlit as st
from src.logo import show_logo
from src.analysis import (
    get_basic_info,
    get_statistics
)

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
    page_title="Analysis",
    page_icon="📊",
    layout="wide"
)
show_logo()



st.title(
    t["analysis"]
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
# GENERAL INFORMATION
# ==========================

st.subheader(
    t["general_info"]
)



info = get_basic_info(
    data
)



col1, col2, col3, col4 = st.columns(4)



with col1:

    st.metric(

        t["rows"],

        info["Nombre de lignes"]

    )



with col2:

    st.metric(

        t["columns"],

        info["Nombre de colonnes"]

    )



with col3:

    st.metric(

        t["missing"],

        info["Valeurs manquantes"]

    )



with col4:

    st.metric(

        t["duplicates"],

        info["Doublons"]

    )



st.divider()



# ==========================
# STATISTICS
# ==========================

st.subheader(
    t["statistics"]
)



statistics = get_statistics(
    data
)



st.dataframe(
    statistics,
    use_container_width=True
)