from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def train_linear_model(df, target_column):
    """
    Entraîner un modèle de régression linéaire
    """

    # Séparer les variables explicatives et la cible
    X = df.drop(columns=[target_column])
    y = df[target_column]


    # Garder uniquement les colonnes numériques
    X = X.select_dtypes(include=["number"])


    # Division des données
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )


    # Création du modèle
    model = LinearRegression()


    # Entraînement
    model.fit(
        X_train,
        y_train
    )


    # Prédiction
    y_pred = model.predict(X_test)


    # Évaluation
    mse = mean_squared_error(
        y_test,
        y_pred
    )

    r2 = r2_score(
        y_test,
        y_pred
    )


    return model, mse, r2
def predict_value(model, input_data):
    """
    Faire une prédiction avec un modèle entraîné
    """

    prediction = model.predict(input_data)

    return prediction[0]
