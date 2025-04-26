import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# --- Page Config ---
st.set_page_config(
    page_title="SLR-ENP Electricity Price Predictor",
    page_icon="⚡",
    layout="centered",  # "wide" also looks good if you have many inputs
    initial_sidebar_state="expanded"
)

# --- Hide Streamlit Default Menu and Footer ---
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- Title Section ---
st.title("⚡ SLR-ENP Electricity Price Predictor ⚡")
st.markdown("""
Welcome to the **SLR-ENP** project!

Predict the electricity price based on your inputs using a trained Machine Learning model.

---
""")

# --- Load the Model ---
model_path = Path("artifacts/model_trainer/SLR_ENP_model.joblib")
model = joblib.load(model_path)

# --- Sidebar ---
st.sidebar.header("Input Features")

year = st.sidebar.number_input("Year", min_value=2000, max_value=2050, step=1)
quarter = st.sidebar.selectbox("Quarter", ["First", "Second", "Third", "Fourth"])
electricity_very_small = st.sidebar.number_input("Electricity: Very Small (Pence per kWh)", min_value=0.0)
electricity_small = st.sidebar.number_input("Electricity: Small (Pence per kWh)", min_value=0.0)
electricity_small_medium = st.sidebar.number_input("Electricity: Small/Medium (Pence per kWh)", min_value=0.0)
electricity_medium = st.sidebar.number_input("Electricity: Medium (Pence per kWh)", min_value=0.0)
electricity_large = st.sidebar.number_input("Electricity: Large (Pence per kWh)", min_value=0.0)
electricity_very_large = st.sidebar.number_input("Electricity: Very Large (Pence per kWh)", min_value=0.0)
electricity_extra_large = st.sidebar.number_input("Electricity: Extra Large (Pence per kWh)", min_value=0.0)

# Calculate Avg_Electricity_Price
avg_electricity_price = (
    electricity_very_small + electricity_small + electricity_small_medium +
    electricity_medium + electricity_large + electricity_very_large +
    electricity_extra_large
) / 7

# --- Predict Button ---
if st.button('🔮 Predict Price'):
    try:
        input_data = {
            'Year': [str(year)],
            'Quarter': [1 if quarter == "First" else 2 if quarter == "Second" else 3 if quarter == "Third" else 4],
            'Electricity: Very Small (Pence per kWh)': [electricity_very_small],
            'Electricity: Small (Pence per kWh)': [electricity_small],
            'Electricity: Small/Medium (Pence per kWh)': [electricity_small_medium],
            'Electricity: Medium (Pence per kWh)': [electricity_medium],
            'Electricity: Large (Pence per kWh)': [electricity_large],
            'Electricity: Very Large (Pence per kWh)': [electricity_very_large],
            'Electricity: Extra Large (Pence per kWh)': [electricity_extra_large],
            'Avg_Electricity_Price': [avg_electricity_price]
        }
        input_df = pd.DataFrame(input_data)

        # Make prediction
        prediction = model.predict(input_df)
        
        # Success Message
        st.success(f"✅ Predicted Electricity Price: **{prediction[0]:.2f}** Pence per kWh")
    except Exception as e:
        st.error(f"❌ Prediction failed: {str(e)}")

# --- Footer ---
st.markdown("---")
st.markdown(
    "Made with ❤️ by [Justice](https://github.com/thekendev)"
)