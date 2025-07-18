import streamlit as st
import pdfplumber
import re

st.set_page_config(page_title="Resume Parser", layout="centered")
st.title("📄 Resume Parsing Web App")
st.markdown("Upload your resume (PDF), and this app will extract key details.")

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    with pdfplumber.open(uploaded_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() + '\n'
    return text

# Function to parse name (simplified)
def extract_name(text):
    lines = text.split('\n')
    return lines[0] if lines else "Not Found"

# Function to extract email
def extract_email(text):
    match = re.search(r"[a-zA-Z0-9\.\-_]+@[a-zA-Z\.\-]+\.[a-zA-Z]{2,}", text)
    return match.group() if match else "Not Found"

# Function to extract phone number
def extract_phone(text):
    match = re.search(r"\+?\d[\d\s\-]{8,13}", text)
    return match.group() if match else "Not Found"

# Upload file
uploaded_file = st.file_uploader("Upload your resume (PDF format only)", type=["pdf"])

if uploaded_file:
    st.info("Extracting data...")
    resume_text = extract_text_from_pdf(uploaded_file)

    name = extract_name(resume_text)
    email = extract_email(resume_text)
    phone = extract_phone(resume_text)

    st.success("✅ Resume Parsed Successfully!")
    st.markdown("### 🔍 Extracted Information:")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")

    with st.expander("📜 Full Resume Text"):
        st.text(resume_text)
