import streamlit as st

from database.mongodb import (students_collection,bmi_collection)

st.title("BMI Calculator")

#Load students from the database
students = list(students_collection.find())

if not students:
    st.warning("No students found. Please register students first.")
    st.stop()

#student Dropdown
student_names = []

for student in students:
    full_name = (student["first_name"] + " " + student["last_name"])
    student_names.append(full_name)

selected_student = st.selectbox("Select a student", student_names)

#BMI Calculation
height = st.number_input("Height (meters)", min_value=0.5, max_value=3.0, value=1.70, step=0.01)

weight = st.number_input("Weight (kilograms)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)

#BMI Calculation
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

#Show BMI Result
st.metric("BMI Score",round(bmi, 2))

st.success(f"Category: {category}")


#Save to Mongodb
bmi_collection.insert_one({
    "student_name": selected_student,
    "height": height,
    "weight": weight,
    "bmi":round(bmi, 2),
    "category": category
})

st.success("BMI report saved successfully!")

#View BMI Reports
st.subheader("BMI Reports")
reports = list(bmi_collection.find())

if reports:
    for report in reports:
        st.write(report["student_name"], "|", report["height"], "m |", report["weight"], "kg |", report["bmi"], "|", report["category"])
else:
    st.warning("No BMI reports found.")

#Summary of BMI Categories
st.subheader("BMI Category Summary")

st.metric("Total BMI Reports", len(reports))