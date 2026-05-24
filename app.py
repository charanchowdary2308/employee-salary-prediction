import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("salary_model.pkl", "rb"))

# Title
st.title("Employee Salary Prediction")

st.write("Enter employee details below:")

# Input fields
age = st.number_input("Age", min_value=18, max_value=100, value=30)

workclass_options = {
    "Private": 0,
    "Self-emp": 1,
    "Government": 2
}

workclass_choice = st.selectbox(
    "Workclass",
    list(workclass_options.keys())
)

workclass = workclass_options[workclass_choice]

education_options = {
    "Bachelors": 0,
    "HS-grad": 1,
    "Masters": 2,
    "Doctorate": 3
}

education_choice = st.selectbox(
    "Education",
    list(education_options.keys())
)

education = education_options[education_choice]


marital_options = {
    "Married": 0,
    "Single": 1,
    "Divorced": 2
}

marital_choice = st.selectbox(
    "Marital Status",
    list(marital_options.keys())
)

marital_status = marital_options[marital_choice]

occupation_options = {
    "Tech-support": 0,
    "Sales": 1,
    "Exec-managerial": 2,
    "Craft-repair": 3
}

occupation_choice = st.selectbox(
    "Occupation",
    list(occupation_options.keys())
)

occupation = occupation_options[occupation_choice]

gender_options = {
    "Male": 1,
    "Female": 0
}

gender_choice = st.selectbox(
    "Gender",
    list(gender_options.keys())
)

gender = gender_options[gender_choice]

capital_gain = st.number_input("Capital Gain", value=0)

capital_loss = st.number_input("Capital Loss", value=0)

hours_per_week = st.number_input("Hours Per Week", value=40)

country_options = {
    "United-States": 0,
    "India": 1,
    "Canada": 2,
    "Mexico": 3
}

country_choice = st.selectbox(
    "Native Country",
    list(country_options.keys())
)

native_country = country_options[country_choice]
# Predict button
if st.button("Predict Income"):

    input_data = np.array([[
        age,
        workclass,
        education,
        marital_status,
        occupation,
        gender,
        capital_gain,
        capital_loss,
        hours_per_week,
        native_country
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Predicted Income: High Income")
    else:
        st.success("Predicted Income: Low Income")