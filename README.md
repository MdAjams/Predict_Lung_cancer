# 🚭 Lung Cancer Prediction Dashboard

## 📌 Project Overview

This project predicts the likelihood of **lung cancer** in patients using their health and lifestyle data. It covers everything from **data preprocessing**, **EDA**, **model training**, to **deployment** via a Streamlit web app.

---

## 📊 Dataset

[Lung Cancer Dataset on Kaggle](https://www.kaggle.com/datasets/iamtanmayshukla/lung-cancer-data?resource=download)

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit
- Pickle

---

## 🔍 Project Workflow

### 1. **Data Preprocessing**
- Label encoding for `GENDER`, `LUNG_CANCER`
- Feature scaling using StandardScaler

### 2. **Exploratory Data Analysis (EDA)**
- Correlation heatmaps
- Class imbalance checks
- Histograms, boxplots, countplots

### 3. **Modeling**
- Logistic Regression (baseline)
- Decision Tree
- Random Forest 🌲 (best performance)
- Support Vector Machine (SVM)

### 4. **Evaluation**
- Accuracy, Precision, Recall, F1-score
- Confusion Matrix
- ROC Curve

### 5. **Deployment**
- Model saved using `pickle`
- Streamlit web app to input patient data and predict lung cancer

---

## 📈 Key Insights

1. **Smoking** is strongly linked to higher lung cancer risk.
2. **Males** show slightly higher incidence.
3. **Age** is a strong predictor.
4. **Random Forest** gave the best performance.
5. Most important features: **Smoking, Age, Fatigue, Chronic Disease**

---

## 💻 Web App Preview

> ✨ User-friendly Streamlit dashboard with:
- KPIs: Total Cases, Cancer Cases, etc.
- Live Prediction: Input form for real-time prediction
- Visuals: Charts, background image, and custom UI

---

## 🧪 Installation & Requirements

Create a virtual environment and run:

```bash
pip install -r requirements.txt
streamlit run main.py
