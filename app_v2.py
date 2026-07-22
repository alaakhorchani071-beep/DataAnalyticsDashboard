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


# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("📊 Data Analytics Dashboard")

st.sidebar.markdown("---")

st.sidebar.success("Bienvenue !")

st.sidebar.write("""
Cette application permet :

✅ Importer des données

✅ Nettoyer les données

✅ Analyse statistique

✅ Visualisation

✅ Machine Learning

✅ Rapport PDF
""")

st.sidebar.markdown("---")

st.sidebar.info(
    "Développé par Alaa Khorchani"
)


# ==========================
# TITRE
# ==========================

st.title("📊 Data Analytics Dashboard")


st.write("""
Application intelligente d'analyse de données.

Fonctionnalités :

- 📂 Importation CSV / Excel
- 🧹 Nettoyage
- 📊 Analyse statistique
- 📈 Visualisation
- 🤖 Machine Learning
- 📄 Rapport PDF
""")


st.divider()


# ==========================
# IMPORTATION
# ==========================

st.subheader("📂 Importer vos données")


uploaded_file = st.file_uploader(
    "Choisissez un fichier CSV ou Excel",
    type=["csv", "xlsx"]
)


if uploaded_file is not None:

    st.write("📄 Fichier sélectionné :", uploaded_file.name)

    data = load_data(uploaded_file)


    if data is not None:

        st.success(
            "✅ Fichier chargé avec succès !"
        )


        # ==========================
        # CREATION DES ONGLETS
        # ==========================

        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "📂 Données",
                "📊 Analyse",
                "📈 Visualisation",
                "🤖 Machine Learning",
                "📄 Rapport"
            ]
        )
                # ==========================
        # ONGLET 1 : DONNEES
        # ==========================

        with tab1:

            st.subheader("📄 Aperçu des données")

            st.dataframe(data)


            st.divider()


            st.subheader("🧹 Nettoyage des données")


            if st.button(
                "🧹 Nettoyer les données"
            ):

                with st.spinner(
                    "Nettoyage en cours..."
                ):

                    cleaned_data = clean_data(data)


                st.success(
                    "✅ Données nettoyées avec succès !"
                )


                st.dataframe(
                    cleaned_data
                )


                csv = cleaned_data.to_csv(
                    index=False
                ).encode("utf-8")


                st.download_button(
                    "📥 Télécharger CSV nettoyé",
                    csv,
                    "cleaned_data.csv",
                    "text/csv"
                )


        # ==========================
        # ONGLET 2 : ANALYSE
        # ==========================

        with tab2:

            st.subheader(
                "📊 Informations générales"
            )


            info = get_basic_info(data)


            col1, col2, col3, col4 = st.columns(4)


            col1.metric(
                "📄 Lignes",
                info["Nombre de lignes"]
            )


            col2.metric(
                "📋 Colonnes",
                info["Nombre de colonnes"]
            )


            col3.metric(
                "❗ Valeurs manquantes",
                info["Valeurs manquantes"]
            )


            col4.metric(
                "🔁 Doublons",
                info["Doublons"]
            )


            st.divider()


            st.subheader(
                "📈 Statistiques descriptives"
            )


            statistics = get_statistics(data)


            st.dataframe(
                statistics
            )


        # ==========================
        # ONGLET 3 : VISUALISATION
        # ==========================

        with tab3:

            st.subheader(
                "📈 Visualisation des données"
            )


            selected_column = st.selectbox(
                "Choisissez une colonne :",
                data.columns
            )


            chart_type = st.selectbox(
                "Type de graphique :",
                [
                    "Histogramme",
                    "Barres",
                    "Courbe",
                    "Diagramme circulaire"
                ]
            )


            if chart_type == "Histogramme":

                fig = create_histogram(
                    data,
                    selected_column
                )


            elif chart_type == "Barres":

                fig = create_bar_chart(
                    data,
                    selected_column
                )


            elif chart_type == "Diagramme circulaire":

                fig = create_pie_chart(
                    data,
                    selected_column
                )


            else:

                fig = create_line_chart(
                    data,
                    selected_column
                )


            st.pyplot(fig)
                    # ==========================
        # ONGLET 4 : MACHINE LEARNING
        # ==========================

        with tab4:

            st.subheader(
                "🤖 Machine Learning"
            )


            numeric_columns = data.select_dtypes(
                include=["number"]
            ).columns


            if len(numeric_columns) > 1:


                target_column = st.selectbox(
                    "Variable à prédire :",
                    numeric_columns
                )


                if st.button(
                    "🚀 Entraîner le modèle"
                ):


                    model, mse, r2 = train_linear_model(
                        data,
                        target_column
                    )


                    st.session_state["model"] = model
                    st.session_state["target"] = target_column


                    st.success(
                        "✅ Modèle entraîné avec succès"
                    )


                    st.write(
                        "📉 MSE :",
                        mse
                    )


                    st.write(
                        "📊 R² :",
                        r2
                    )


                if "model" in st.session_state:


                    st.subheader(
                        "🔮 Faire une prédiction"
                    )


                    target = st.session_state["target"]


                    features = data.drop(
                        columns=[target]
                    ).select_dtypes(
                        include=["number"]
                    ).columns


                    user_input = {}


                    for feature in features:

                        user_input[feature] = st.number_input(
                            f"Entrer {feature}",
                            value=0.0
                        )


                    if st.button(
                        "🔮 Prédire"
                    ):


                        input_df = pd.DataFrame(
                            [user_input]
                        )


                        prediction = predict_value(
                            st.session_state["model"],
                            input_df
                        )


                        st.success(
                            f"Résultat prédit : {prediction:.2f}"
                        )


            else:

                st.warning(
                    "Il faut au moins deux colonnes numériques."
                )



        # ==========================
        # ONGLET 5 : RAPPORT PDF
        # ==========================

        with tab5:

            st.subheader(
                "📄 Rapport automatique"
            )


            info = get_basic_info(data)

            statistics = get_statistics(data)


            if st.button(
                "📄 Créer le rapport PDF"
            ):


                file = generate_report(
                    info,
                    statistics
                )


                with open(
                    file,
                    "rb"
                ) as pdf:


                    st.download_button(
                        label="📥 Télécharger le rapport PDF",
                        data=pdf,
                        file_name="Data_Analytics_Report.pdf",
                        mime="application/pdf"
                    )