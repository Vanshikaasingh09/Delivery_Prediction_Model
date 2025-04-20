import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load("delivery_time_classifier.pkl")

# App title
st.title("📦 Delivery Time Range Predictor")

# Sidebar inputs
st.sidebar.header("📋 Order Details")

order_day = st.sidebar.selectbox("Order Day (1=Mon, 7=Sun)", list(range(1, 8)))
order_hour = st.sidebar.slider("Order Hour (24hr format)", 0, 23, 16)
available_tomorrow = st.sidebar.selectbox("User Available Tomorrow?", [0, 1])
available_evening = st.sidebar.selectbox("User Available in Evening?", [0, 1])

# Create input DataFrame
input_df = pd.DataFrame([{
    'order_day': order_day,
    'order_hour': order_hour,
    'user_available_tomorrow': available_tomorrow,
    'user_available_evening': available_evening
}])

# Predict
if st.sidebar.button("Predict Delivery Time Range"):
    prediction = model.predict(input_df)[0]
    emoji_map = {
        "Morning": "🌅",
        "Afternoon": "☀️",
        "Evening": "🌇",
        "Night": "🌙"
    }
    st.success(f"Predicted Delivery Time Range: **{prediction}** {emoji_map.get(prediction, '')}")
