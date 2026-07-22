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


# Création base de données
create_database()


# ==========================
# CHOIX DE LA LANGUE
# ==========================

language = st.sidebar.selectbox(
    "🌍 Language",
    list(translations.keys())
)

t = translations[language]


# ==========================
# SIDEBAR
# ==========================

st.sidebar.title(t["title"])

st.sidebar.markdown("---")

st.sidebar.success(
    t["welcome"]
)


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


st.sidebar.markdown("---")


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
    type=["csv", "xlsx"]
)



if uploaded_file is not None:


    data = load_data(uploaded_file)


    if data is not None:


        st.success(
            t["success_upload"]
        )
                # ==========================
        # CREATION DES ONGLETS
        # ==========================

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
        # ONGLET 1 : DONNEES
        # ==========================

        with tab1:

            st.subheader(
                t["preview"]
            )

            st.dataframe(data)


            st.divider()


            st.subheader(
                t["clean"]
            )


            if st.button(
                t["clean"]
            ):

                with st.spinner(
                    t["cleaning"]
                ):

                    cleaned_data = clean_data(data)


                st.success(
                    t["clean_success"]
                )


                st.dataframe(
                    cleaned_data
                )


                csv = cleaned_data.to_csv(
                    index=False
                ).encode("utf-8")


                st.download_button(
                    t["download_clean"],
                    csv,
                    "cleaned_data.csv",
                    "text/csv"
                )



        # ==========================
        # ONGLET 2 : ANALYSE
        # ==========================

        with tab2:


            st.subheader(
                t["general_info"]
            )


            info = get_basic_info(data)


            col1, col2, col3, col4 = st.columns(4)


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


            st.divider()


            st.subheader(
                t["statistics"]
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
                t["visualization"]
            )


            selected_column = st.selectbox(
                t["choose_column"],
                data.columns
            )


            chart_type = st.selectbox(
                t["chart_type"],
                [
                    t["histogram"],
                    t["bar"],
                    t["line"],
                    t["pie"]
                ]
            )


            if chart_type == t["histogram"]:

                fig = create_histogram(
                    data,
                    selected_column
                )


            elif chart_type == t["bar"]:

                fig = create_bar_chart(
                    data,
                    selected_column
                )


            elif chart_type == t["pie"]:

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
                t["machine_learning"]
            )


            numeric_columns = data.select_dtypes(
                include=["number"]
            ).columns



            if len(numeric_columns) > 1:


                target_column = st.selectbox(
                    "Target",
                    numeric_columns
                )


                if st.button(
                    t["train"]
                ):


                    model, mse, r2 = train_linear_model(
                        data,
                        target_column
                    )


                    st.session_state["model"] = model
                    st.session_state["target"] = target_column


                    st.success(
                        t["model_success"]
                    )


                    st.write(
                        "MSE :",
                        mse
                    )


                    st.write(
                        "R² :",
                        r2
                    )



                if "model" in st.session_state:


                    st.subheader(
                        t["predict"]
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
                            feature,
                            value=0.0
                        )



                    if st.button(
                        t["predict"]
                    ):


                        input_df = pd.DataFrame(
                            [user_input]
                        )


                        prediction = predict_value(
                            st.session_state["model"],
                            input_df
                        )


                        st.success(
                            f"{t['prediction_result']} : {prediction:.2f}"
                        )



            else:

                st.warning(
                    t["warning_numeric"]
                )




        # ==========================
        # ONGLET 5 : RAPPORT PDF
        # ==========================

        with tab5:


            st.subheader(
                t["report"]
            )


            info = get_basic_info(data)

            statistics = get_statistics(data)



            if st.button(
                t["create_report"]
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
                        t["download_report"],
                        pdf,
                        "Data_Analytics_Report.pdf",
                        "application/pdf"
                    )
                    