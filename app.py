import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("⚖️ BMI Calculator")
st.markdown("Calculate your **Body Mass Index** using weight (kg) and height (m).")

st.divider()

weight = st.number_input("Weight (kg)", min_value=1.0, max_value=500.0, value=70.0, step=0.1)
height = st.number_input("Height (m)", min_value=0.1, max_value=3.0, value=1.75, step=0.01)

if st.button("Calculate BMI"):
    bmi = weight / (height * height)
    st.metric(label="Your BMI", value=f"{bmi:.2f}")

    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
    elif bmi < 25.0:
        category = "Normal weight"
        color = "green"
    elif bmi < 30.0:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obese"
        color = "red"

    st.markdown(f"**Category:** :{color}[{category}]")

st.divider()
st.caption("Formula: BMI = Weight / (Height × Height)")
