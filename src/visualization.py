import matplotlib.pyplot as plt


def create_histogram(df, column):
    fig, ax = plt.subplots()

    ax.hist(df[column].dropna(), bins=20)

    ax.set_title(f"Distribution de {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Fréquence")

    return fig


def create_bar_chart(df, column):
    fig, ax = plt.subplots()

    df[column].value_counts().plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(f"Répartition de {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Nombre")

    return fig


def create_line_chart(df, column):
    fig, ax = plt.subplots()

    ax.plot(df[column].dropna())

    ax.set_title(f"Evolution de {column}")
    ax.set_xlabel("Index")
    ax.set_ylabel(column)

    return fig
def create_pie_chart(df, column):
    fig, ax = plt.subplots()

    values = df[column].value_counts()

    ax.pie(
        values,
        labels=values.index,
        autopct="%1.1f%%"
    )

    ax.set_title(f"Répartition de {column}")

    return fig
