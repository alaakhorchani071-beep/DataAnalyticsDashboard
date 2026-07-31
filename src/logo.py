from PIL import Image
import streamlit as st
import os


def show_logo():

    logo_path = "logo.png.png"

    if os.path.exists(logo_path):

        logo = Image.open(logo_path)

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:

            st.image(
                logo,
                width=180
            )

    else:

        st.warning("Logo not found")