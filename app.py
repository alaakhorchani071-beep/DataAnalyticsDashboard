from PIL import Image
from src.auth import login_user, register_user
from src.database import create_database
from translations import translations

import streamlit as st
import sqlite3


# ==========================
# CONFIGURATION
# ==========================

st.set_page_config(
    page_title="Data Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)
logo = Image.open("logo.png.png")

st.sidebar.image(
    logo,
    width=150
)


create_database()



# ==========================
# LANGUAGE SYSTEM
# ==========================

if "language" not in st.session_state:

    st.session_state["language"] = "Français"



t = translations[
    st.session_state["language"]
]



# ==========================
# AUTHENTIFICATION
# ==========================

if "user" not in st.session_state:


    st.sidebar.title(
        t["account"]
    )


    choice = st.sidebar.selectbox(
        t["account"],
        [
            t["login"],
            t["register"]
        ]
    )



    username = st.sidebar.text_input(
        t["username"]
    )


    password = st.sidebar.text_input(
        t["password"],
        type="password"
    )



    # ==========================
    # REGISTER
    # ==========================

    if choice == t["register"]:


        email = st.sidebar.text_input(
            "Email"
        )


        language = st.sidebar.selectbox(
            t["language"],
            [
                "Français",
                "English",
                "العربية"
            ]
        )



        if st.sidebar.button(
            t["register"]
        ):


            result = register_user(
                username,
                email,
                password,
                language
            )



            if result:


                st.session_state["user"] = username

                st.session_state["language"] = language



                st.success(
                    translations[language]["register_success"]
                )


                st.rerun()



            else:


                st.error(
                    translations[language]["user_exists"]
                )




    # ==========================
    # LOGIN
    # ==========================

    else:


        if st.sidebar.button(
            t["login"]
        ):


            result = login_user(
                username,
                password
            )



            if result:


                st.session_state["user"] = username



                # ==========================
                # RECUPERATION LANGUE
                # ==========================

                connection = sqlite3.connect(
                    "database.db"
                )


                cursor = connection.cursor()


                cursor.execute(
                    """
                    SELECT language
                    FROM users
                    WHERE username = ?
                    """,
                    (username,)
                )


                user_language = cursor.fetchone()


                connection.close()



                if user_language:

                    st.session_state["language"] = user_language[0]



                st.success(
                    translations[
                        st.session_state["language"]
                    ]["login_success"]
                )


                st.rerun()



            else:


                st.error(
                    t["wrong_login"]
                )



    st.stop()



# ==========================
# APPLICATION
# ==========================


t = translations[
    st.session_state["language"]
]



st.sidebar.success(
    f"{t['welcome']} {st.session_state['user']} 👋"
)



# ==========================
# CHANGE LANGUAGE
# ==========================

language = st.sidebar.selectbox(
    t["language"],
    [
        "Français",
        "English",
        "العربية"
    ],
    index=[
        "Français",
        "English",
        "العربية"
    ].index(
        st.session_state["language"]
    )
)



if language != st.session_state["language"]:


    st.session_state["language"] = language


    st.rerun()



# ==========================
# LOGOUT
# ==========================

if st.sidebar.button(
    t["logout"]
):


    del st.session_state["user"]


    st.rerun()




# ==========================
# HOME PAGE
# ==========================


st.title(
    t["title"]
)
st.write(
    t["description"]
)