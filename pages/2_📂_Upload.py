import streamlit as st
import sqlite3

from src.upload import load_data


st.set_page_config(
    page_title="Upload Data",
    page_icon="📂",
    layout="wide"
)


st.title("📂 Upload your data")


# Vérification connexion

if "user" not in st.session_state:

    st.warning(
        "⚠️ Please login first."
    )

    st.stop()



username = st.session_state["user"]



st.write(
"""
Import your CSV or Excel file to start analysis.
"""
)



uploaded_file = st.file_uploader(
    "Choose a CSV or Excel file",
    type=["csv", "xlsx"]
)



if uploaded_file is not None:


    data = load_data(uploaded_file)


    if data is not None:


        st.success(
            "✅ File uploaded successfully!"
        )



        # Sauvegarde dans la session

        st.session_state["data"] = data



        # ==========================
        # ENREGISTREMENT HISTORIQUE
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
        # AFFICHAGE
        # ==========================


        st.subheader(
            "📄 Data Preview"
        )


        st.dataframe(
            data
        )



        col1, col2 = st.columns(2)



        with col1:

            st.metric(
                "Rows",
                data.shape[0]
            )



        with col2:

            st.metric(
                "Columns",
                data.shape[1]
            )



else:

    st.info(
        "Please upload a file."
    )