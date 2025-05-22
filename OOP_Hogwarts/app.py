# main streamlit file

# Streamlit UI Logic (Abstraction, Instantiation, Callable Objects etc.)

from PIL import Image
import streamlit as st
from classes.student import Student
from classes.teacher import Teacher
from classes.classroom import Classroom
from utils.helpers import load_students, save_students
import os

# Page Config
st.set_page_config(page_title="OOP Hogwarts", layout="centered")

# Add Hogwarts Banner Image
img_path = os.path.join("assets", "hogwart_magic.png")
image = Image.open(img_path)
st.image("assets/hogwart_magic.png", use_container_width=True)

# Title Section
st.markdown("<h1 style='text-align: center; color: #6A1B9A;'>🧙‍♂️ OOP Hogwarts School of Code & Magic</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #8E24AA;'>Where Python meets Potions and OOP meets Magic!</h4>", unsafe_allow_html=True)

# Load initial data
data = load_students()
students = []
for d in data:
    s = Student(d["name"], d["house"], d["marks"])
    students.append(s)

# Setup Hogwarts Classroom
teacher = Teacher("McGonagall", "Transfiguration")
classroom = Classroom("Magical OOPs 101", teacher)
for s in students:
    classroom.add_student(s)

# Add new student
st.subheader("🔮 Enroll New Student")
with st.form("new_student"):
    name = st.text_input("Student Name")
    house = st.selectbox("House", ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"])
    marks = st.slider("Initial Marks", 0, 100, 50)
    submitted = st.form_submit_button("Enroll")
    if submitted and name:
        new_stu = Student(name, house, marks)
        classroom.add_student(new_stu)
        students.append(new_stu)
        save_students([{"name": s.name, "house": s.house, "marks": s.marks} for s in students])
        st.success(f"{name} enrolled into {house}!")

# Show classroom details
st.subheader("🏫 Classroom Summary")
info = classroom.display_info()
st.write(f"👩‍🏫 Teacher: {info['Teacher']}")
st.write(f"📚 Total Students: {len(classroom)}")

# Show all students
st.subheader("📋 Enrolled Students")
for stu in classroom:
    st.markdown(f"- {stu.display_info()}")
