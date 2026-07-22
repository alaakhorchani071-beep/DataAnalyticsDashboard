from src.auth import login_user, register_user
from src.database import create_database

from src.visualization import (
    create_histogram,
    create_bar_chart,
    create_line_chart,
    create_pie_chart
)

from src.analysis import get_basic_info, get_statistics
from src.upload import load_data
from src.model import train_linear_model, predict_value
from src.cleaning import clean_data
from src.report import generate_report

from translations import translations

import streamlit as st
import pandas as pd


# ==========================
# CONFIGURATION
# ==========================

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

    st.sidebar.subheader("🔐 Compte utilisateur")


    choice = st.sidebar.selectbox(
        "Choisir une action",
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


        if st.sidebar.button("Créer un compte"):

            result = register_user(
                username,
                password
            )


            if result:

                st.session_state["user"] = username

                st.sidebar.success(
                    "Compte créé avec succès"
                )

                st.rerun()


            else:

                st.sidebar.error(
                    "Utilisateur existe déjà"
                )


    else:


        if st.sidebar.button("Connexion"):


            result = login_user(
                username,
                password
            )


            if result:

                st.session_state["user"] = username

                st.sidebar.success(
                    "Connexion réussie"
                )

                st.rerun()


            else:

                st.sidebar.error(
                    "Identifiants incorrects"
                )


    st.stop()



# ==========================
# DECONNEXION
# ==========================

st.sidebar.success(
    f"Bienvenue {st.session_state['user']} 👋"
)


if st.sidebar.button("🚪 Déconnexion"):

    del st.session_state["user"]

    st.rerun()



# ==========================
# LANGUE
# ==========================

language = st.sidebar.selectbox(
    "🌍 Language",
    list(translations.keys())
)


t = translations[language]



# ==========================
# SIDEBAR
# ==========================

st.sidebar.title(
    t["title"]
)


st.sidebar.markdown("---")


st.sidebar.write(
f"""
✅ {t["import"]}

✅ {t["clean"]}

✅ {t["analysis"]}

✅ {t["visualization"]}

✅ {t["machine_learning"]}

✅ {t["report"]}
"""
)


st.sidebar.info(
"Développé par Alaa Khorchani"
)



# ==========================
# TITRE
# ==========================

st.title(
    t["title"]
)


st.write(
    t["description"]
)


st.divider()



# ==========================
# IMPORTATION
# ==========================

st.subheader(
    t["upload"]
)


uploaded_file = st.file_uploader(
    t["choose_file"],
    type=["csv","xlsx"]
)



if uploaded_file:


    data = load_data(
        uploaded_file
    )


    if data is not None:


        st.success(
            t["success_upload"]
        )


        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                t["data"],
                t["analysis"],
                t["visualization"],
                t["machine_learning"],
                t["report"]
            ]
        )



        # ==========================
        # DONNEES
        # ==========================

        with tab1:


            st.subheader(
                t["preview"]
            )


            st.dataframe(data)



            st.subheader(
                t["clean"]
            )


            if st.button(
                t["clean"]
            ):


                cleaned_data = clean_data(
                    data
                )


                st.success(
                    "✅ Nettoyage terminé"
                )


                st.dataframe(
                    cleaned_data
                )



        # ==========================
        # ANALYSE
        # ==========================

        with tab2:


            info = get_basic_info(
                data
            )


            col1,col2,col3,col4 = st.columns(4)


            col1.metric(
                t["rows"],
                info["Nombre de lignes"]
            )


            col2.metric(
                t["columns"],
                info["Nombre de colonnes"]
            )


            col3.metric(
                t["missing"],
                info["Valeurs manquantes"]
            )


            col4.metric(
                t["duplicates"],
                info["Doublons"]
            )


            st.dataframe(
                get_statistics(data)
            )



        # ==========================
        # VISUALISATION
        # ==========================

        with tab3:


            column = st.selectbox(
                t["choose_column"],
                data.columns
            )


            chart = st.selectbox(
                t["chart_type"],
                [
                    "Histogramme",
                    "Barres",
                    "Courbe",
                    "Diagramme circulaire"
                ]
            )


            if chart=="Histogramme":

                fig=create_histogram(
                    data,column
                )


            elif chart=="Barres":

                fig=create_bar_chart(
                    data,column
                )


            elif chart=="Diagramme circulaire":

                fig=create_pie_chart(
                    data,column
                )


            else:

                fig=create_line_chart(
                    data,column
                )


            st.pyplot(fig)



        # ==========================
        # MACHINE LEARNING
        # ==========================

        with tab4:


            numeric=data.select_dtypes(
                include=["number"]
            ).columns


            if len(numeric)>1:


                target=st.selectbox(
                    "Target",
                    numeric
                )


                if st.button(
                    t["train"]
                ):


                    model,mse,r2=train_linear_model(
                        data,
                        target
                    )


                    st.session_state["model"]=model
                    st.session_state["target"]=target


                    st.success(
                        "Modèle entraîné"
                    )


                    st.write("MSE :",mse)
                    st.write("R² :",r2)



            else:

                st.warning(
                    "Il faut deux colonnes numériques"
                )



        # ==========================
        # RAPPORT
        # ==========================

        with tab5:


            if st.button(
                t["create_report"]
            ):


                file=generate_report(
                    get_basic_info(data),
                    get_statistics(data)
                )


                with open(file,"rb") as pdf:


                    st.download_button(
                        t["download_report"],
                        pdf,
                        "report.pdf",
                        "application/pdf"
                    )
                