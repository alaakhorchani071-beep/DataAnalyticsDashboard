import pandas as pd
import streamlit as st

def load_data(file):

    try:

        if file.name.endswith(".csv"):

            df = pd.read_csv(file)


        elif file.name.endswith(".xlsx"):

            df = pd.read_excel(
                file,
                engine="openpyxl"
            )


        else:

            return None


        return df


    except Exception as e:

        st.error(f"Erreur lors du chargement : {e}")

        return None