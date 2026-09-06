import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Newborn Baby Heart Risk Predictor",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

model = joblib.load("newborn_risk_model.pkl")

# -------------------- STYLE --------------------
st.markdown("""
<style>
/* Main page */
.stApp {
    background: linear-gradient(135deg, #fffaf0 0%, #f2fbf7 100%);
}

.block-container {
    max-width: 1500px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

/* Header */
.header {
    background: linear-gradient(90deg, #fff8f4, #eef7ff);
    border-radius: 18px;
    padding: 22px 30px;
    margin-bottom: 22px;
    border: 1px solid #dce7f4;
    text-align: center;
}

.header-title {
    color: #204a8e;
    font-size: 36px;
    font-weight: 800;
    margin: 0;
}

.header-subtitle {
    color: #52657a;
    font-size: 15px;
    margin-top: 6px;
}

/* Section */
.section {
    background: rgba(255,255,255,0.82);
    border: 1px solid #d7e2ee;
    border-radius: 18px;
    padding: 24px 28px 28px 28px;
    box-shadow: 0 5px 18px rgba(31, 67, 110, 0.08);
}

.section-title {
    color: #204a8e;
    font-size: 23px;
    font-weight: 750;
    margin-bottom: 18px;
}

/* Streamlit labels */
label, .stNumberInput label, .stSelectbox label {
    color: #17366f !important;
    font-weight: 650 !important;
    font-size: 15px !important;
}

/* Inputs */
div[data-testid="stNumberInput"] input {
    background: #ffffff !important;
    border: 1px solid #bfd1e7 !important;
    border-radius: 10px !important;
    color: #172b4d !important;
}

div[data-baseweb="select"] > div {
    background-color: white !important;
    border: 1px solid #bfd1e7 !important;
    border-radius: 10px !important;
}

div[data-baseweb="select"] * {
    color: #172b4d !important;
}

div[data-baseweb="popover"] {
    background-color: white !important;
}

div[data-baseweb="popover"] > div {
    background-color: white !important;
}

div[data-baseweb="popover"] * {
    background-color: white !important;
    color: #172b4d !important;
}

/* Dropdown options */
[role="option"] {
    background-color: white !important;
    color: #172b4d !important;
}

[role="option"]:hover {
    background-color: #eef5ff !important;
    color: #172b4d !important;
}

[aria-selected="true"] {
    background-color: #e8f1ff !important;
    color: #173f91 !important;
}
.stSelectbox div[data-baseweb="select"] span {
    color: #172b4d !important;
    opacity: 1 !important;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 54px;
    margin-top: 12px;
    border-radius: 11px;
    border: none;
    background: linear-gradient(90deg, #2463b5, #1d579f);
    color: white;
    font-size: 18px;
    font-weight: 750;
}

/* Result */
.result-box {
    margin-top: 24px;
    padding: 25px;
    background: rgba(255,255,255,0.92);
    border: 1px solid #d7e9df;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0 5px 18px rgba(31, 67, 110, 0.08);
}

.result-title {
    color: #204a8e;
    font-size: 25px;
    font-weight: 800;
    margin-bottom: 14px;
}

.risk-value {
    display: inline-block;
    min-width: 280px;
    padding: 15px 35px;
    border-radius: 14px;
    font-size: 31px;
    font-weight: 800;
}

.healthy {
    background: #e6f7e9;
    color: #16833d;
}

.atrisk {
    background: #fff4d6;
    color: #b46b00;
}

.highrisk {
    background: #ffe6e6;
    color: #c62828;
}

.note {
    color: #617184;
    font-size: 14px;
    margin-top: 12px;
}

/* Hide Streamlit footer/menu for cleaner presentation */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


# -------------------- HEADER --------------------
st.markdown("""
<div class="header">
    <div class="header-title">🫀 Newborn Baby Heart Risk Predictor</div>
    <div class="header-subtitle">
        Enter the newborn baby details below to predict the heart risk level.
    </div>
</div>
""", unsafe_allow_html=True)


# -------------------- INPUT SECTION --------------------
st.markdown("""
<div class="section">
<div class="section-title">📋 Newborn Baby Details</div>
""", unsafe_allow_html=True)

left, right = st.columns(2, gap="large")

with left:
    gest_age = st.number_input(
        "Gestational Age (weeks)",
        min_value=28.0, max_value=42.0, value=37.5, step=0.1
    )

    birth_weight = st.number_input(
        "Birth Weight (kg)",
        min_value=0.5, max_value=6.0, value=2.76, step=0.01
    )

    heart_rate = st.number_input(
        "Heart Rate (bpm)",
        min_value=50, max_value=220, value=145, step=1
    )

    spo2 = st.number_input(
        "Oxygen Saturation (%)",
        min_value=50.0, max_value=100.0, value=93.0, step=0.1
    )

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=34.0, max_value=40.0, value=37.3, step=0.1
    )

    feeding = st.number_input(
        "Feeding Frequency per Day",
        min_value=0, max_value=15, value=9, step=1
    )

with right:
    resp_rate = st.number_input(
        "Respiratory Rate (bpm)",
        min_value=10, max_value=90, value=30, step=1
    )

    apgar = st.number_input(
        "Apgar Score",
        min_value=0, max_value=10, value=10, step=1
    )

    urine = st.number_input(
        "Urine Output Count (per day)",
        min_value=0, max_value=20, value=8, step=1
    )

    jaundice = st.number_input(
        "Jaundice Level (mg/dL)",
        min_value=0.0, max_value=20.0, value=2.8, step=0.1
    )

    sex = st.selectbox(
        "Sex",
        ["Female", "Male"]
    )

    oxygen = st.selectbox(
        "Oxygen Given",
        ["No", "Yes"]
    )

    resuscitation = st.selectbox(
        "Resuscitation Required",
        ["No", "Yes"]
    )

st.markdown("</div>", unsafe_allow_html=True)

# -------------------- PREDICT --------------------
st.write("")

if st.button("📊  Predict Heart Risk Level"):

    input_data = pd.DataFrame([{
        "Sex": sex,
        "Gestational_Age_weeks": gest_age,
        "Birth_Weight_kg": birth_weight,
        "Heart_Rate_bpm": heart_rate,
        "Respiratory_Rate_bpm": resp_rate,
        "Oxygen_Saturation_percent": spo2,
        "Feeding_Frequency_per_day": feeding,
        "Urine_Output_Count": urine,
        "Jaundice_Level_mg_dL": jaundice,
        "Temperature_C": temperature,
        "Apgar_Score": apgar,
        "Oxygen_Given": 1 if oxygen == "Yes" else 0,
        "Resuscitation_Required": 1 if resuscitation == "Yes" else 0
    }])

    prediction = model.predict(input_data)[0]

    if prediction == "Healthy":
        css_class = "healthy"
        icon = "💚"
    elif prediction == "At Risk":
        css_class = "atrisk"
        icon = "⚠️"
    else:
        css_class = "highrisk"
        icon = "🚨"

    st.markdown(f"""
    <div class="result-box">
        <div class="result-title">Predicted Risk Level</div>
        <div class="risk-value {css_class}">
            {icon} {prediction}
        </div>
        <div class="note">
            Prediction generated from the entered newborn baby parameters.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.warning(
        "This application is a machine-learning demonstration using synthetic data. "
        "It is not a medical diagnosis or a substitute for professional neonatal care."
    )
