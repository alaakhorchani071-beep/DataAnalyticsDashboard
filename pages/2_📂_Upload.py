import streamlit as st
import sqlite3
from src.upload import load_data
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
    page_title="Upload Data",
    page_icon="📂",
    layout="wide"
)
show_logo()



st.title(
    t["upload"]
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
# INTRODUCTION
# ==========================

st.write(
    t["choose_file"]
)



# ==========================
# FILE UPLOAD
# ==========================

uploaded_file = st.file_uploader(

    t["choose_file"],

    type=[
        "csv",
        "xlsx"
    ]

)



if uploaded_file is not None:


    data = load_data(
        uploaded_file
    )


    if data is not None:



        st.success(
            t["success_upload"]
        )



        # Save data

        st.session_state["data"] = data



        # ==========================
        # HISTORY
        # ==========================

        connection = sqlite3.connect(
            "database.db"
        )


        cursor = connection.cursor()



        cursor.execute(
            """
            SELECT *
            FROM history
            WHERE username = ?
            AND filename = ?
            AND action = ?
            """,
            (
                username,
                uploaded_file.name,
                "Analysis"
            )
        )



        exists = cursor.fetchone()



        if not exists:


            cursor.execute(
                """
                INSERT INTO history
                (
                    username,
                    filename,
                    action
                )

                VALUES (?, ?, ?)

                """,
                (
                    username,
                    uploaded_file.name,
                    "Analysis"
                )
            )


            connection.commit()



        connection.close()



        # ==========================
        # PREVIEW
        # ==========================

        st.subheader(
            t["data_preview"]
        )



        st.dataframe(
            data,
            use_container_width=True
        )



        col1, col2 = st.columns(2)



        with col1:


            st.metric(

                t["rows"],

                data.shape[0]

            )



        with col2:


            st.metric(

                t["columns"],

                data.shape[1]

            )



else:


    st.info(
        t["upload_first"]
    )