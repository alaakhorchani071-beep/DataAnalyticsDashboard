def get_basic_info(df):
    info = {}

    info["Nombre de lignes"] = df.shape[0]
    info["Nombre de colonnes"] = df.shape[1]
    info["Valeurs manquantes"] = df.isnull().sum().sum()
    info["Doublons"] = df.duplicated().sum()

    return info


def get_statistics(df):
    return df.describe()