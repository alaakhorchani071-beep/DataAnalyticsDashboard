from reportlab.lib.pagesizes import letter

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

import matplotlib.pyplot as plt
import os



def generate_report(
        info,
        statistics,
        data,
        ml_results=None,
        filename="Data_Analytics_Report.pdf"
):


    doc = SimpleDocTemplate(
        filename,
        pagesize=letter
    )


    styles = getSampleStyleSheet()

    content = []



    # ==========================
    # TITLE
    # ==========================

    content.append(
        Paragraph(
            "📊 Data Analytics Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1,20)
    )



    # ==========================
    # GENERAL INFORMATION
    # ==========================

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



    info_table = Table(
        info_data
    )


    info_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    0.5,
                    colors.black
                ),

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,0),
                    colors.lightgrey
                )
            ]
        )
    )


    content.append(
        info_table
    )


    content.append(
        Spacer(1,20)
    )



    # ==========================
    # STATISTICS
    # ==========================

    content.append(
        Paragraph(
            "Descriptive Statistics",
            styles["Heading2"]
        )
    )


    statistics_data = [
        list(statistics.columns)
    ]



    for row in statistics.values:

        statistics_data.append(
            [
                str(x)
                for x in row
            ]
        )



    stats_table = Table(
        statistics_data,
        repeatRows=1
    )



    stats_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    0.5,
                    colors.black
                ),

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,0),
                    colors.lightgrey
                )
            ]
        )
    )


    content.append(
        stats_table
    )


    content.append(
        Spacer(1,20)
    )



    # ==========================
    # VISUALIZATIONS
    # ==========================

    content.append(
        Paragraph(
            "Data Visualizations",
            styles["Heading2"]
        )
    )


    numeric_columns = data.select_dtypes(
        include="number"
    ).columns



    # Histogram

    if len(numeric_columns) > 0:


        column = numeric_columns[0]


        plt.figure(
            figsize=(6,4)
        )


        plt.hist(
            data[column],
            bins=20
        )


        plt.title(
            f"Histogram - {column}"
        )


        plt.xlabel(
            column
        )


        plt.ylabel(
            "Frequency"
        )


        image_path = "histogram.png"



        plt.savefig(
            image_path,
            bbox_inches="tight"
        )


        plt.close()



        content.append(
            Image(
                image_path,
                width=400,
                height=250
            )
        )



    # Bar Chart


    if len(data.columns) > 0:


        column = data.columns[0]


        values = data[column].value_counts().head(10)



        plt.figure(
            figsize=(6,4)
        )


        values.plot(
            kind="bar"
        )


        plt.title(
            f"Bar Chart - {column}"
        )


        image_path = "bar_chart.png"



        plt.savefig(
            image_path,
            bbox_inches="tight"
        )


        plt.close()



        content.append(
            Image(
                image_path,
                width=400,
                height=250
            )
        )



    # ==========================
    # MACHINE LEARNING RESULTS
    # ==========================

    if ml_results is not None:


        content.append(
            Spacer(1,20)
        )


        content.append(
            Paragraph(
                "Machine Learning Results",
                styles["Heading2"]
            )
        )


        ml_data = [

            ["Metric", "Value"],

            [
                "Model",
                ml_results["model_name"]
            ],

            [
                "MAE",
                round(
                    ml_results["mae"],
                    3
                )
            ],

            [
                "RMSE",
                round(
                    ml_results["rmse"],
                    3
                )
            ],

            [
                "R² Score",
                round(
                    ml_results["r2"],
                    3
                )
            ],

            [
                "Features",
                ", ".join(
                    ml_results["features"]
                )
            ]

        ]



        ml_table = Table(
            ml_data
        )



        ml_table.setStyle(
            TableStyle(
                [
                    (
                        "GRID",
                        (0,0),
                        (-1,-1),
                        0.5,
                        colors.black
                    ),

                    (
                        "BACKGROUND",
                        (0,0),
                        (-1,0),
                        colors.lightgrey
                    )
                ]
            )
        )



        content.append(
            ml_table
        )



    # ==========================
    # BUILD PDF
    # ==========================

    doc.build(
        content
    )



    # ==========================
    # REMOVE TEMP FILES
    # ==========================

    for img in [
        "histogram.png",
        "bar_chart.png"
    ]:

        if os.path.exists(img):

            os.remove(img)



    return filename