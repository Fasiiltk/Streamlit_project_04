import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("tip_prediction_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Tip Prediction App 💰")

st.markdown("### Predict the tip amount based on total bill, time, and number of people.")

# User Inputs
total_bill = st.number_input("Enter Total Bill Amount ($)", min_value=0.0, format="%.2f")
time = st.selectbox("Select Time", ["Lunch", "Dinner"])
size = st.number_input("Enter Number of People", min_value=1, step=1)

# Encode Time (Lunch = 0, Dinner = 1)
time_encoded = 1 if time == "Dinner" else 0

# Prediction Button
if st.button("Predict Tip"):
    test_data = pd.DataFrame([[total_bill, time_encoded, size]], columns=['total_bill', 'time', 'size'])
    predicted_tip = model.predict(test_data)
    
    # Display result
    st.success(f"Predicted Tip: **${predicted_tip[0]:.2f}** 💵")


