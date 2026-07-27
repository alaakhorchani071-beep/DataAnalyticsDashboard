from datetime import datetime
import os
import matplotlib.pyplot as plt

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)


def generate_report(
    info,
    statistics,
    data,
    username,
    ml_results=None,
    filename="Data_Analytics_Report.pdf"
):

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    content = []

    # =====================================================
    # TITLE
    # =====================================================

    content.append(
        Paragraph(
            "📊 Data Analytics Dashboard Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    today = datetime.now().strftime("%d/%m/%Y %H:%M")

    content.append(
        Paragraph(
            f"<b>User :</b> {username}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Generated on :</b> {today}",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # =====================================================
    # GENERAL INFORMATION
    # =====================================================

    content.append(
        Paragraph(
            "General Information",
            styles["Heading2"]
        )
    )

    info_data = [
        ["Information", "Value"]
    ]

    for key, value in info.items():

        info_data.append(
            [
                str(key),
                str(value)
            ]
        )

    info_table = Table(info_data)

    info_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )
    )

    content.append(info_table)

    content.append(
        Spacer(1, 20)
    )

    # =====================================================
    # DESCRIPTIVE STATISTICS
    # =====================================================

    content.append(
        Paragraph(
            "Descriptive Statistics",
            styles["Heading2"]
        )
    )

    statistics_data = []

    statistics_data.append(
        ["Index"] + list(statistics.columns)
    )

    for index, row in statistics.iterrows():

        statistics_data.append(
            [str(index)] + [str(value) for value in row]
        )

    stats_table = Table(
        statistics_data,
        repeatRows=1
    )

    stats_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )
    )

    content.append(stats_table)

    content.append(
        Spacer(1, 20)
    )
        # =====================================================
    # DATA VISUALIZATIONS
    # =====================================================

    content.append(
        Paragraph(
            "Data Visualizations",
            styles["Heading2"]
        )
    )

    numeric_columns = data.select_dtypes(
        include="number"
    ).columns

    # -------------------------
    # HISTOGRAM
    # -------------------------

    if len(numeric_columns) > 0:

        column = numeric_columns[0]

        plt.figure(figsize=(6, 4))

        plt.hist(
            data[column].dropna(),
            bins=20,
            edgecolor="black"
        )

        plt.title(f"Histogram - {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")

        histogram_path = "histogram.png"

        plt.savefig(
            histogram_path,
            bbox_inches="tight"
        )

        plt.close()

        content.append(
            Image(
                histogram_path,
                width=420,
                height=250
            )
        )

        content.append(
            Spacer(1, 15)
        )

    # -------------------------
    # BAR CHART
    # -------------------------

    if len(data.columns) > 0:

        column = data.columns[0]

        values = data[column].value_counts().head(10)

        plt.figure(figsize=(6, 4))

        values.plot(kind="bar")

        plt.title(f"Bar Chart - {column}")

        bar_chart_path = "bar_chart.png"

        plt.savefig(
            bar_chart_path,
            bbox_inches="tight"
        )

        plt.close()

        content.append(
            Image(
                bar_chart_path,
                width=420,
                height=250
            )
        )

        content.append(
            Spacer(1, 15)
        )

    # -------------------------
    # PIE CHART
    # -------------------------

    if len(data.columns) > 0:

        column = data.columns[0]

        values = data[column].value_counts().head(6)

        plt.figure(figsize=(5, 5))

        plt.pie(
            values,
            labels=values.index,
            autopct="%1.1f%%"
        )

        plt.title(f"Pie Chart - {column}")

        pie_chart_path = "pie_chart.png"

        plt.savefig(
            pie_chart_path,
            bbox_inches="tight"
        )

        plt.close()

        content.append(
            Image(
                pie_chart_path,
                width=350,
                height=350
            )
        )

        content.append(
            Spacer(1, 15)
        )

    # -------------------------
    # LINE CHART
    # -------------------------

    if len(numeric_columns) > 0:

        column = numeric_columns[0]

        plt.figure(figsize=(6, 4))

        plt.plot(
            data[column].reset_index(drop=True)
        )

        plt.title(f"Line Chart - {column}")

        line_chart_path = "line_chart.png"

        plt.savefig(
            line_chart_path,
            bbox_inches="tight"
        )

        plt.close()

        content.append(
            Image(
                line_chart_path,
                width=420,
                height=250
            )
        )

        content.append(
            Spacer(1, 20)
        )

    # =====================================================
    # MACHINE LEARNING RESULTS
    # =====================================================

    if ml_results is not None:

        content.append(
            Paragraph(
                "Machine Learning Results",
                styles["Heading2"]
            )
        )

        ml_data = [

            ["Metric", "Value"],

            ["Model", ml_results["model_name"]],

            ["MAE", round(ml_results["mae"], 3)],

            ["RMSE", round(ml_results["rmse"], 3)],

            ["R² Score", round(ml_results["r2"], 3)],

            ["Features", ", ".join(ml_results["features"])]

        ]

        ml_table = Table(ml_data)

        ml_table.setStyle(
            TableStyle(
                [
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ]
            )
        )

        content.append(ml_table)

        content.append(
            Spacer(1, 20)
        )
            # =====================================================
    # AUTOMATIC INSIGHTS
    # =====================================================

    content.append(
        Paragraph(
            "💡 Data Insights",
            styles["Heading2"]
        )
    )


    rows = data.shape[0]

    columns = data.shape[1]

    missing_values = data.isnull().sum().sum()


    insights = [

        f"Dataset contains {rows} rows and {columns} columns.",

        f"Total missing values: {missing_values}.",

    ]


    numeric_count = len(
        data.select_dtypes(
            include="number"
        ).columns
    )


    insights.append(
        f"Number of numerical columns: {numeric_count}."
    )


    if ml_results is not None:

        insights.append(
            f"Best trained model: {ml_results['model_name']}."
        )

        insights.append(
            f"Model R² Score: {round(ml_results['r2'],3)}."
        )



    for text in insights:

        content.append(
            Paragraph(
                "• " + text,
                styles["Normal"]
            )
        )


        content.append(
            Spacer(1,5)
        )
            # =====================================================
    # END OF REPORT
    # =====================================================

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "End of Report",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            "This report was automatically generated by the Data Analytics Dashboard application.",
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1, 10)
    )

    content.append(
        Paragraph(
            f"Generated on: {today}",
            styles["Normal"]
        )
    )

    # =====================================================
    # BUILD PDF
    # =====================================================

    doc.build(content)

    # =====================================================
    # DELETE TEMPORARY IMAGES
    # =====================================================

    images = [
        "histogram.png",
        "bar_chart.png",
        "pie_chart.png",
        "line_chart.png"
    ]

    for image in images:

        if os.path.exists(image):
            os.remove(image)

    return filename