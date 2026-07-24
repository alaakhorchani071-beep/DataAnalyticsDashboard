from src.auth import login_user, register_user
from src.database import create_database

import streamlit as st


st.set_page_config(
    page_title="Data Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)


create_database()



# ==========================
# AUTHENTIFICATION
# ==========================

if "user" not in st.session_state:


    st.sidebar.title("🔐 Compte")


    choice = st.sidebar.selectbox(
        "Action",
        [
            "Connexion",
            "Créer un compte"
        ]
    )


    username = st.sidebar.text_input(
        "Nom utilisateur"
    )


    password = st.sidebar.text_input(
        "Mot de passe",
        type="password"
    )


    if choice == "Créer un compte":


        email = st.sidebar.text_input(
            "Email"
        )


        language = st.sidebar.selectbox(
            "🌍 Langue",
            [
                "Français",
                "English",
                "العربية"
            ]
        )


        if st.sidebar.button(
            "Créer un compte"
        ):


            result = register_user(
                username,
                email,
                password,
                language
            )


            if result:

                st.session_state["user"] = username

                st.success(
                    "Compte créé avec succès"
                )

                st.rerun()


            else:

                st.error(
                    "Utilisateur existe déjà"
                )



    else:


        if st.sidebar.button(
            "Connexion"
        ):


            result = login_user(
                username,
                password
            )


            if result:

                st.session_state["user"] = username

                st.success(
                    "Connexion réussie"
                )

                st.rerun()


            else:

                st.error(
                    "Identifiants incorrects"
                )


    st.stop()



# ==========================
# APPLICATION
# ==========================


st.sidebar.success(
    f"Bienvenue {st.session_state['user']} 👋"
)



if st.sidebar.button(
    "🚪 Déconnexion"
):

    del st.session_state["user"]

    st.rerun()



st.title(
    "📊 Data Analytics Dashboard"
)


st.write(
    """
Bienvenue dans votre application.

Utilisez le menu à gauche pour accéder aux fonctionnalités.
"""
)
