import streamlit as st
import numpy as np
import pandas as pd
import pickle
import plotly.express as px

# Page Config (Must be First Streamlit Command)
st.set_page_config(page_title="Lung Cancer Prediction Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv('preprocessed_lung_cancer.csv')  # Update path if local testing

# Load Pre-trained Model
@st.cache_resource
def load_model():
    with open('lung_cancer_model.pkl', 'rb') as f:   # Update path if local testing
        return pickle.load(f)

data = load_data()
model = load_model()

# Streamlit sidebar with logo
st.sidebar.image("images/Background.jpeg", width=300)

# Sidebar: Patient Input
st.sidebar.header("📋 Patient Information")
def user_input():
    GENDER = st.sidebar.selectbox("Gender", ("M", "F"))
    AGE = st.sidebar.slider("Age", 20, 90, 45)
    SMOKING = st.sidebar.selectbox("Smoking", (0, 1))
    YELLOW_FINGERS = st.sidebar.selectbox("Yellow Fingers", (0, 1))
    ANXIETY = st.sidebar.selectbox("Anxiety", (0, 1))
    PEER_PRESSURE = st.sidebar.selectbox("Peer Pressure", (0, 1))
    CHRONIC_DISEASE = st.sidebar.selectbox("Chronic Disease", (0, 1))
    FATIGUE = st.sidebar.selectbox("Fatigue", (0, 1))
    ALLERGY = st.sidebar.selectbox("Allergy", (0, 1))
    WHEEZING = st.sidebar.selectbox("Wheezing", (0, 1))
    ALCOHOL_CONSUMING = st.sidebar.selectbox("Alcohol Consuming", (0, 1))
    COUGHING = st.sidebar.selectbox("Coughing", (0, 1))
    SHORTNESS_OF_BREATH = st.sidebar.selectbox("Shortness of Breath", (0, 1))
    SWALLOWING_DIFFICULTY = st.sidebar.selectbox("Swallowing Difficulty", (0, 1))
    CHEST_PAIN = st.sidebar.selectbox("Chest Pain", (0, 1))
    
    gender_encoded = 1 if GENDER == "M" else 0
    
    user_data = np.array([[gender_encoded, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE,
                           CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING,
                           COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
    return user_data

input_data = user_input()

# Prediction Button
if st.sidebar.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1] * 100
    st.subheader("🧠 Prediction Result")
    st.markdown(f"### 🎯 **Risk Level**: {'🔴 High Risk' if prediction == 1 else '🟢 Low Risk'}")
    st.progress(int(proba))
    st.markdown(f"**Probability of Lung Cancer:** `{proba:.2f}%`")

# Main Title
st.title("🚭 Lung Cancer Prediction Dashboard")
# Background image
st.image("images/Lungs.jpg", caption="Lung Cancer Prediction", use_column_width=True)

# Key Stats (Mock Data)
st.subheader("📈 Key Program Statistics")
# Create 4 columns for KPI cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div style='background-color: #1f77b4; padding: 20px; border-radius: 15px; color: white; text-align: center;'>
            <h4>🏥 Referrals</h4>
            <h2>1,272</h2>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='background-color: #d62728; padding: 20px; border-radius: 15px; color: white; text-align: center;'>
            <h4>🫁 Lung Cancer</h4>
            <h2>164</h2>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style='background-color: #2ca02c; padding: 20px; border-radius: 15px; color: white; text-align: center;'>
            <h4>🌬️ COPD Cases</h4>
            <h2>15</h2>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div style='background-color: #ff7f0e; padding: 20px; border-radius: 15px; color: white; text-align: center;'>
            <h4>🫒 Trachea Cases</h4>
            <h2>9</h2>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# EDA Visualizations
st.subheader("📊 Data Sample")
st.dataframe(data.head())

st.subheader("🧍 Gender Distribution")
gender_count = data["GENDER"].value_counts().reset_index()
gender_count.columns = ["Gender", "Count"]
fig_gender = px.bar(gender_count, x="Gender", y="Count", color="Gender")
st.plotly_chart(fig_gender, use_container_width=True)

st.subheader("📅 Age vs Lung Cancer")
if 'AGE' in data.columns and 'LUNG_CANCER' in data.columns:
    fig_age = px.histogram(data, x="AGE", color="LUNG_CANCER", barmode="group")
    st.plotly_chart(fig_age, use_container_width=True)

st.subheader("📆 Assessment Productivity (Mock Data)")
mock_productivity = pd.DataFrame({
    "Month": pd.date_range(start="2023-01-01", periods=6, freq="M").strftime("%b %Y"),
    "Assessments": [120, 140, 110, 160, 180, 200]
})
fig_prod = px.bar(mock_productivity, x="Month", y="Assessments")
st.plotly_chart(fig_prod, use_container_width=True)

st.subheader("🔄 Screening Funnel (Mock Data)")
funnel_df = pd.DataFrame({
    'Stage': ['Clinical Suspicion', 'CT Scheduled', 'CT Completed', 'Referred', 'Diagnosed'],
    'Count': [8379, 2735, 2395, 147, 164]
})
funnel_chart = px.funnel(funnel_df, x='Count', y='Stage')
st.plotly_chart(funnel_chart, use_container_width=True)

st.markdown("---")
st.markdown("✨ Inspired by Lucem Health’s Lung Cancer Dashboard")
