import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("🩺 Diabetes Prediction App for Females")
st.markdown("""
This **machine learning** app predicts whether a Female has diabetes based on various medical attributes.
Enter the required data in the sidebar to get started:
""")

st.sidebar.header("📋 Input Features")
pregnancies = st.sidebar.number_input("Pregnancies", 0, 20, 1)
glucose = st.sidebar.number_input("Glucose", 0, 200, 110)
blood_pressure = st.sidebar.number_input("Blood Pressure", 0, 140, 70)
skin_thickness = st.sidebar.number_input("Skin Thickness", 0, 100, 20)
insulin = st.sidebar.number_input("Insulin", 0, 900, 80)
bmi = st.sidebar.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.sidebar.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
age = st.sidebar.number_input("Age", 10, 100, 30)

predict_clicked = st.sidebar.button("Predict")

st.subheader("🎯 Prediction Result")
if predict_clicked:
    data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    scaled_input = scaler.transform(data)
    prediction = model.predict(scaled_input)

    if prediction[0] == 1:
        st.error("The model predicts that the individual **has diabetes**.")
    else:
        st.success("The model predicts that the individual **does not have diabetes**.")
else:
    st.info("Click the **Predict** button to generate the prediction result.")

st.markdown("---")
st.caption("Made by Anshuman Dash | AIML Project")