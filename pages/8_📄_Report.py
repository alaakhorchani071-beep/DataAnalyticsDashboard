import streamlit as st
import sqlite3
import base64


from src.analysis import get_basic_info, get_statistics
from src.report import generate_report



# ==========================
# CONFIGURATION PAGE
# ==========================

st.set_page_config(
    page_title="Report",
    page_icon="📄",
    layout="wide"
)


st.title(
    "📄 Data Analytics Report"
)



# ==========================
# VERIFICATION USER
# ==========================

if "user" not in st.session_state:

    st.warning(
        "⚠️ Please login first."
    )

    st.stop()



username = st.session_state["user"]



# ==========================
# VERIFICATION DATA
# ==========================

if "data" not in st.session_state:

    st.info(
        "📂 Please upload data first."
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
    "👁️ Report Preview"
)



st.write(
    "### 📌 General Information"
)


for key, value in info.items():

    st.write(
        f"**{key} :** {value}"
    )



st.divider()



st.write(
    "### 📊 Descriptive Statistics"
)


st.dataframe(
    statistics,
    use_container_width=True
)



# ==========================
# ML RESULTS PREVIEW
# ==========================

st.divider()


st.write(
    "### 🤖 Machine Learning Results"
)



if "ml_results" in st.session_state:


    ml_results = st.session_state["ml_results"]


    st.success(
        "✅ ML results available"
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
        f"**R² Score :** {round(ml_results['r2'],3)}"
    )



else:

    ml_results = None


    st.info(
        "ℹ️ Train a model first to add ML results."
    )



st.divider()



# ==========================
# CREATE PDF
# ==========================

st.subheader(
    "📄 Generate PDF"
)



if st.button(
    "🚀 Create PDF Report"
):


    filename = generate_report(
        info,
        statistics,
        data,
        ml_results
    )



    # ==========================
    # SAVE HISTORY
    # ==========================

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
        "✅ Report created successfully!"
    )



# ==========================
# PDF PREVIEW
# ==========================

if "pdf_file" in st.session_state:


    filename = st.session_state["pdf_file"]



    st.divider()


    st.subheader(
        "👁️ PDF Preview"
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
        label="📥 Download PDF",
        data=pdf_bytes,
        file_name=filename,
        mime="application/pdf"
    )