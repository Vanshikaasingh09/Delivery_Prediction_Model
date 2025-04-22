This project predicts the expected time of arrival (ETA) for orders using historical data from
orders_data.xlsx.
It aims to help logistics companies estimate delivery times more accurately.
Features:
- Load and preprocess order data from Excel
- Feature engineering based on order and dispatch details
- Predict arrival time using machine learning

Dataset:
orders_data.xlsx contains the following columns (example):
- Order ID
- Order Date
- Dispatch Time
- Distance (km)
- Vehicle Type
- Destination
  
Model Info:
The model uses features like:
- Order time and dispatch time
- Distance to destination
- Vehicle type
- Day of week / time of day
  
Tech stack:
- pandas for data handling
- scikit-learn for modeling
- Streamlit for visualization
Output:
https://deliverypredictionmodel-bbqscrbnnzxayg3drq3ogc.streamlit.app/

Future Enhancements:
- Add weather or traffic data
- Use geolocation APIs for route info
- Include live ETA updates with real-time input
