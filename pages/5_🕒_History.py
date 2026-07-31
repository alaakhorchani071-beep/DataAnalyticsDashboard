import streamlit as st
import sqlite3
import pandas as pd

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
    page_title="History",
    page_icon="🕒",
    layout="wide"
)



st.title(
    t["history"]
)



# ==========================
# CHECK LOGIN
# ==========================

if "user" not in st.session_state:


    st.warning(
        "⚠️ " + t["login"]
    )


    st.stop()



username = st.session_state["user"]



# ==========================
# DATABASE
# ==========================

connection = sqlite3.connect(
    "database.db"
)



query = """
SELECT *
FROM history
WHERE username = ?
"""



history = pd.read_sql_query(
    query,
    connection,
    params=(username,)
)



connection.close()



# ==========================
# DISPLAY HISTORY
# ==========================

if len(history) == 0:


    st.info(
        t["no_history"]
    )


else:


    st.dataframe(
        history,
        use_container_width=True
    )