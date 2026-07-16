import pandas as pd


def remove_duplicates(df):
    """
    Supprimer les lignes en double
    """

    df = df.drop_duplicates()

    return df



def handle_missing_values(df):
    """
    Traiter les valeurs manquantes
    """

    for column in df.columns:

        # Colonne numérique
        if pd.api.types.is_numeric_dtype(df[column]):

            df[column] = df[column].fillna(
                df[column].mean()
            )


        # Colonne texte
        else:

            df[column] = df[column].fillna(
                df[column].mode()[0]
            )


    return df



def clean_data(df):
    """
    Appliquer toutes les étapes de nettoyage
    """

    df = remove_duplicates(df)

    df = handle_missing_values(df)

    return df
