import streamlit as st
import pandas as pd
import pickle
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Setup Gemini
if api_key:
    genai.configure(api_key=api_key)
    llm = genai.GenerativeModel('gemini-2.5-flash')
else:
    st.error("API Key not found. Please check your .env file.")

# Load the trained model
model = pickle.load(open('crop_model.pkl', 'rb'))

st.set_page_config(page_title="AgriOracle AI", page_icon="🌱")
st.title("🌱 AgriOracle AI")
st.markdown("### Precision Agriculture Decision Engine")

# Sidebar for simplified inputs based on your Excel file
st.sidebar.header("Environmental Inputs")
temp = st.sidebar.slider("Temperature (°C)", 0.0, 50.0, 25.0)
hum = st.sidebar.slider("Humidity (%)", 0.0, 100.0, 70.0)
ph = st.sidebar.slider("Soil pH", 0.0, 14.0, 6.5)
rain = st.sidebar.number_input("Rainfall (mm)", value=100.0)
region = st.text_input("Enter Region/State", "Tamil Nadu")

if st.button("Predict Optimal Crop"):
    # Match the model's feature order: Temperature, Humidity, pH, Rainfall
    input_features = [[temp, hum, ph, rain]]
    prediction = model.predict(input_features)[0]
    
    st.success(f"AgriOracle Recommends: **{prediction.upper()}**")
    
    # Explainable AI (XAI) via Gemini
    with st.spinner("Analyzing profitability and regional suitability..."):
        prompt = (f"In {region}, the environmental conditions are: Temperature {temp}°C, "
                  f"Humidity {hum}%, Soil pH {ph}, and Rainfall {rain}mm. "
                  f"The ML model recommends '{prediction}'. "
                  f"Provide a brief technical justification for why this crop fits these metrics "
                  f"and explain its market profitability potential.")
        
        response = llm.generate_content(prompt)
        st.markdown("### 💡 AI Insights & Logic")
        st.info(response.text)