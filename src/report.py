from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(info, statistics, filename="Data_Analytics_Report.pdf"):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []


    # Titre

    title = Paragraph(
        "Data Analytics Dashboard Report",
        styles["Title"]
    )

    content.append(title)

    content.append(Spacer(1, 20))


    # Informations générales

    content.append(
        Paragraph(
            "Informations générales :",
            styles["Heading2"]
        )
    )


    for key, value in info.items():

        content.append(
            Paragraph(
                f"{key} : {value}",
                styles["Normal"]
            )
        )


    content.append(
        Spacer(1, 20)
    )


    # Statistiques

    content.append(
        Paragraph(
            "Statistiques descriptives :",
            styles["Heading2"]
        )
    )


    statistics_text = statistics.to_string()


    content.append(
        Paragraph(
            statistics_text.replace("\n", "<br/>"),
            styles["Normal"]
        )
    )


    doc.build(content)


    return filename