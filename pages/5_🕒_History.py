import streamlit as st
import sqlite3
import pandas as pd


st.set_page_config(
    page_title="History",
    page_icon="🕒",
    layout="wide"
)


st.title("🕒 History")



connection = sqlite3.connect(
    "database.db"
)


query = """
SELECT *
FROM history
"""


history = pd.read_sql_query(
    query,
    connection
)


connection.close()



if len(history) == 0:

    st.info(
        "No history available."
    )

else:

    st.dataframe(
        history,
        use_container_width=True
    )