import streamlit as st
import sqlite3
import base64

from src.logo import show_logo
from src.analysis import get_basic_info, get_statistics
from src.report import generate_report

from translations import translations


# ==========================
# CONFIGURATION
# ==========================

st.set_page_config(
    page_title="Report",
    page_icon="📄",
    layout="wide"
)


# ==========================
# LANGUAGE SYSTEM
# ==========================

language = st.session_state.get(
    "language",
    "Français"
)

t = translations[language]


# ==========================
# LOGO
# ==========================

show_logo()



# ==========================
# TITLE
# ==========================

st.title(
    t.get("report", "📄 Report")
)



# ==========================
# CHECK USER
# ==========================

if "user" not in st.session_state:

    st.warning(
        "⚠️ " + t.get("login", "Login required")
    )

    st.stop()



username = st.session_state["user"]



# ==========================
# CHECK DATA
# ==========================

if "data" not in st.session_state:

    st.info(
        t.get(
            "upload_first",
            "📂 Please upload data first."
        )
    )

    st.stop()



data = st.session_state["data"]



# ==========================
# ANALYSIS
# ==========================

info = get_basic_info(data)

statistics = get_statistics(data)



# ==========================
# REPORT PREVIEW
# ==========================

st.subheader(
    t.get(
        "report_preview",
        "👁️ Report Preview"
    )
)



st.write(
    f"### 📌 {t.get('general_info','General Information')}"
)



for key, value in info.items():

    st.write(
        f"**{key} :** {value}"
    )



st.divider()



st.write(
    f"### 📊 {t.get('statistics','Statistics')}"
)



st.dataframe(
    statistics,
    use_container_width=True
)



# ==========================
# MACHINE LEARNING RESULTS
# ==========================

st.divider()



st.write(
    f"### 🤖 {t.get('ml_results','Machine Learning Results')}"
)



if "ml_results" in st.session_state:


    ml_results = st.session_state["ml_results"]


    st.success(
        t.get(
            "ml_available",
            "✅ ML results available"
        )
    )


    st.write(
        f"**Model :** {ml_results['model_name']}"
    )


    st.write(
        f"**MAE :** {round(ml_results['mae'],3)}"
    )


    st.write(
        f"**RMSE :** {round(ml_results['rmse'],3)}"
    )


    st.write(
        f"**R² :** {round(ml_results['r2'],3)}"
    )



else:


    ml_results = None


    st.info(
        t.get(
            "train_first",
            "ℹ️ Train a model first."
        )
    )



# ==========================
# CREATE PDF
# ==========================

st.divider()



st.subheader(
    t.get(
        "create_report",
        "📄 Create Report"
    )
)



if st.button(
    t.get(
        "generate_pdf",
        "🚀 Generate PDF"
    )
):


    filename = generate_report(

        info,

        statistics,

        data,

        username,

        ml_results

    )



    # SAVE HISTORY

    connection = sqlite3.connect(
        "database.db"
    )


    cursor = connection.cursor()



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
            filename,
            "Report"
        )
    )



    connection.commit()

    connection.close()



    st.session_state["pdf_file"] = filename



    st.success(
        t.get(
            "report_generated",
            "✅ Report generated successfully"
        )
    )



# ==========================
# PDF PREVIEW
# ==========================

if "pdf_file" in st.session_state:


    filename = st.session_state["pdf_file"]



    st.divider()



    st.subheader(
        t.get(
            "pdf_preview",
            "👁️ PDF Preview"
        )
    )



    with open(
        filename,
        "rb"
    ) as pdf:


        pdf_bytes = pdf.read()



    base64_pdf = base64.b64encode(
        pdf_bytes
    ).decode(
        "utf-8"
    )



    pdf_display = f"""
    <iframe
        src="data:application/pdf;base64,{base64_pdf}"
        width="100%"
        height="700"
        type="application/pdf">
    </iframe>
    """



    st.markdown(
        pdf_display,
        unsafe_allow_html=True
    )



    st.download_button(

        label=t.get(
            "download_report",
            "📥 Download PDF"
        ),

        data=pdf_bytes,

        file_name=filename,

        mime="application/pdf"

    )