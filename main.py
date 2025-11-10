import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Streamlit app title and description
st.title("BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) to assess your body weight category.")

# Input fields for weight and height
weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (m):", min_value=0.5, step=0.01)

# Button to calculate BMI
if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    st.subheader(f"Your BMI is: {bmi}")
    st.write(f"Category: **{category}**")

    # Optional feedback based on category
    if category == "Underweight":
        st.info("You are underweight. Consider consulting a healthcare provider for guidance.")
    elif category == "Normal weight":
        st.success("You are within the normal range. Maintain a balanced diet and regular exercise!")
    elif category == "Overweight":
        st.warning("You are slightly overweight. Regular physical activity and healthy eating may help.")
    else:
        st.error("You are in the obesity range. It's recommended to seek advice from a healthcare provider.")
