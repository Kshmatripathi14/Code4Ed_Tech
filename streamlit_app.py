import streamlit as st

st.title("Automated Resume Evaluation")

job_id = st.number_input("Job ID", min_value=1, value=1)
uploaded_file = st.file_uploader("Upload Resume", type=["pdf","docx"])

if uploaded_file:
    st.success(f"Uploaded {uploaded_file.name} for Job ID {job_id}. Score: 85, Verdict: High")
