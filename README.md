# 📊 Data Analytics Dashboard

## 📌 Description

Data Analytics Dashboard est une application web interactive développée avec **Python** et **Streamlit**. Elle permet aux utilisateurs d'importer des fichiers CSV ou Excel, de nettoyer les données, de les analyser, de créer des visualisations interactives, d'entraîner un modèle de Machine Learning et de générer un rapport PDF.

Ce projet a été réalisé dans le but de mettre en pratique les compétences en analyse de données, visualisation et apprentissage automatique.

---

## 🚀 Fonctionnalités

- 📂 Importation de fichiers CSV et Excel
- 🧹 Nettoyage automatique des données
  - Suppression des doublons
  - Gestion des valeurs manquantes
- 📊 Analyse exploratoire des données
  - Nombre de lignes
  - Nombre de colonnes
  - Valeurs manquantes
  - Doublons
  - Statistiques descriptives
- 📈 Visualisations interactives
  - Histogramme
  - Diagramme en barres
  - Courbe
  - Diagramme circulaire
- 🤖 Machine Learning
  - Régression linéaire
  - Évaluation du modèle (MSE et R²)
  - Prédiction à partir de nouvelles valeurs
- 📄 Génération d'un rapport PDF
- 📥 Téléchargement des données nettoyées

---

## 🛠️ Technologies utilisées

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- ReportLab

---

## 📁 Structure du projet

```
DataAnalyticsDashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── src/
    ├── analysis.py
    ├── cleaning.py
    ├── model.py
    ├── report.py
    ├── upload.py
    └── visualization.py
```

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/alaakhorchani071-beep/DataAnalyticsDashboard.git
```

### 2. Accéder au projet

```bash
cd DataAnalyticsDashboard
```

### 3. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 4. Activer l'environnement virtuel

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 5. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Exécuter l'application

```bash
streamlit run app.py
```

L'application sera accessible à l'adresse :

```
http://localhost:8501
```

---

## 📸 Aperçu de l'application

Vous pouvez ajouter ici des captures d'écran de votre dashboard.

Exemple :

```
screenshots/dashboard.png
```

---

## 🎯 Compétences mises en œuvre

- Analyse de données
- Nettoyage des données
- Visualisation de données
- Machine Learning
- Développement d'applications avec Streamlit
- Génération de rapports PDF
- Gestion de projet avec Git et GitHub

---

## 📈 Améliorations futures

- Ajout de nouveaux graphiques (Heatmap, Scatter Plot, Box Plot)
- Support de plusieurs modèles de Machine Learning
- Tableau de bord avec navigation par onglets
- Déploiement en ligne
- Authentification des utilisateurs

---

## 👩‍💻 Auteur

**Alaa Khorchani**

Étudiante en Mathématiques Appliquées – Spécialité Data Science

GitHub : https://github.com/alaakhorchani071-beep

---

## 📄 Licence

Ce projet est publié à des fins d'apprentissage et de démonstration.