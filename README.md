# 📊 Data Analytics Dashboard

## 📌 Description

**Data Analytics Dashboard** is an interactive Data Science web application developed with **Python and Streamlit**.

The application provides a complete data analysis workflow, including data importation, cleaning, visualization, Machine Learning modeling, prediction, and automatic PDF report generation.

The objective of this project is to transform raw datasets into meaningful insights through an interactive dashboard.

---

# 🚀 Features

## 📂 Data Importation

- Import CSV and Excel files.
- Automatic dataset loading.
- Dataset preview.
- Display dataset information.

---

## 🧹 Data Cleaning

- Detect missing values.
- Handle missing data.
- Remove duplicates.
- Export cleaned datasets.

---

## 📊 Data Analysis

The dashboard provides:

- Number of rows.
- Number of columns.
- Missing values.
- Duplicate values.
- Data types information.
- Descriptive statistics.

---

## 📈 Data Visualization

Interactive visualizations including:

- Histogram.
- Bar chart.
- Line chart.
- Pie chart.

Users can select:
- The column to analyze.
- The visualization type.

---

# 🤖 Machine Learning

The application supports multiple regression models:

- Linear Regression.
- Decision Tree Regressor.
- Random Forest Regressor.

Features:

- Select target variable.
- Select feature variables.
- Train Machine Learning models.
- Evaluate model performance.

Evaluation metrics:

- MAE (Mean Absolute Error).
- RMSE (Root Mean Square Error).
- R² Score.

Additional features:

- Actual vs Prediction visualization.
- Feature importance analysis.
- Save trained model for future predictions.

---

# 🔮 Prediction

Users can:

- Load the trained model.
- Enter new input values.
- Generate predictions.

---

# 📄 Automatic Report Generation

Generate professional PDF reports containing:

- Dataset information.
- Statistical analysis.
- Data visualizations.
- Machine Learning results.

The generated report can be:

- Previewed directly inside the application.
- Downloaded as PDF.

---

# 🕒 History Management

The application stores user actions using SQLite:

- Generated reports history.
- User activity tracking.

---

# 🛠 Technologies Used

## Programming Language

- Python

## Libraries

- Pandas → Data manipulation
- NumPy → Numerical computation
- Matplotlib → Data visualization
- Streamlit → Interactive dashboard
- Scikit-learn → Machine Learning models
- ReportLab → PDF generation
- SQLite → Database management
- Joblib → Model saving

## Tools

- VS Code
- Git
- GitHub

---

# 📁 Project Structure

```
DataAnalyticsDashboard/

│
├── app.py
│
├── pages/
│   │
│   ├── 1_📊_Dashboard.py
│   ├── 2_📂_Upload.py
│   ├── 3_🧹_Cleaning.py
│   ├── 4_📈_Visualization.py
│   ├── 5_🤖_Machine_Learning.py
│   ├── 6_🔮_Prediction.py
│   ├── 7_📄_Report.py
│   └── 8_🕒_History.py
│
├── src/
│   │
│   ├── analysis.py
│   ├── cleaning.py
│   ├── model.py
│   ├── report.py
│   ├── upload.py
│   └── visualization.py
│
├── models/
│   └── model.pkl
│
├── database.db
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/alaakhorchani071-beep/DataAnalyticsDashboard.git
```

Navigate to the project folder:

```bash
cd DataAnalyticsDashboard
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser.

---

# 📊 Application Workflow

```
Upload Dataset
        ↓
Data Cleaning
        ↓
Data Analysis
        ↓
Visualization
        ↓
Machine Learning Training
        ↓
Prediction
        ↓
PDF Report Generation
```

---

# 🎯 Objectives

- Develop a complete Data Science application.
- Practice data analysis workflows.
- Apply Machine Learning models.
- Create interactive dashboards.
- Improve Python and Streamlit skills.

---

# 👩‍💻 Author

**Alaa Khorchani**

Data Science Student

GitHub:
https://github.com/alaakhorchani071-beep

---

# 🚀 Future Improvements

- Add classification models.
- Add correlation heatmaps.
- Add interactive Plotly visualizations.
- Deploy the application online.
- Improve UI/UX design.
