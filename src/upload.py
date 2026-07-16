import pandas as pd

def load_data(file):
    """
    Charger un fichier CSV ou Excel
    """

    if file.name.endswith(".csv"):
        df = pd.read_csv(file)

    elif file.name.endswith(".xlsx"):
        df = pd.read_excel(file)

    else:
        return None

    return df