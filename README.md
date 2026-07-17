# 📊 Data Analytics Dashboard

## 📌 Description

**Data Analytics Dashboard** is an interactive web application developed with **Python and Streamlit** that allows users to analyze, visualize, clean data, apply Machine Learning models, and generate automatic reports.

This project aims to provide a complete data analysis workflow, from data importation to prediction and reporting.

---

# 🚀 Features

## 📂 Data Importation
- Import CSV and Excel files.
- Automatic loading and display of datasets.
- Data preview.

## 🧹 Data Cleaning
- Detection and handling of missing values.
- Data cleaning process.
- Export cleaned datasets as CSV files.

## 📊 Data Analysis
- Display general information:
  - Number of rows.
  - Number of columns.
  - Missing values.
  - Duplicate values.
- Generate descriptive statistics.

## 📈 Data Visualization
Interactive visualization with:
- Histogram.
- Bar chart.
- Line chart.
- Pie chart.

Users can select the column and the type of visualization.

## 🤖 Machine Learning
- Train a Linear Regression model.
- Select the target variable.
- Evaluate the model using:
  - Mean Squared Error (MSE).
  - R² Score.
- Make predictions using user inputs.

## 📄 Automatic Report Generation
- Generate a PDF report containing:
  - Dataset information.
  - Statistical analysis.

---

# 🛠 Technologies Used

## Programming Language
- Python

## Libraries

- Pandas → Data manipulation and analysis
- NumPy → Numerical computation
- Matplotlib → Data visualization
- Streamlit → Interactive web application
- Scikit-learn → Machine Learning models

## Tools

- VS Code
- Git & GitHub

---

# 📁 Project Structure

```
DataAnalyticsDashboard/

│
├── app.py                    # Main Streamlit application
│
├── requirements.txt          # Project dependencies
│
├── README.md                 # Project documentation
│
├── src/
│   │
│   ├── analysis.py           # Statistical analysis functions
│   ├── cleaning.py           # Data cleaning functions
│   ├── model.py              # Machine Learning functions
│   ├── report.py             # PDF report generation
│   ├── upload.py             # Data loading functions
│   └── visualization.py      # Visualization functions
│
└── Data_Analytics_Report.pdf # Generated report
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/alaakhorchani071-beep/DataAnalyticsDashboard.git
```

## 2. Navigate to the project folder

```bash
cd DataAnalyticsDashboard
```

## 3. Create a virtual environment

```bash
python -m venv .venv
```

## 4. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Launch the Streamlit dashboard:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 📊 Application Workflow

```
Upload Dataset
        ↓
Data Cleaning
        ↓
Statistical Analysis
        ↓
Visualization
        ↓
Machine Learning Prediction
        ↓
PDF Report Generation
```

---

# 🎯 Objectives

- Practice Data Analysis workflow.
- Develop interactive dashboards.
- Apply Machine Learning techniques.
- Improve Python programming skills.
- Build a complete Data Science project.

---

# 👩‍💻 Author

**Alaa Khorchani**

Data Science Student

GitHub:
https://github.com/alaakhorchani071-beep

---

# 📌 Future Improvements

- Add more Machine Learning models:
  - Decision Tree
  - Random Forest
  - Support Vector Machine

- Add advanced visualizations:
  - Correlation heatmap
  - Scatter plots
  - Interactive charts

- Improve dashboard design with custom themes.

---

⭐ If you find this project useful, feel free to give it a star!