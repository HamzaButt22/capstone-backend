import streamlit as st
import requests

st.set_page_config(page_title="AI Capstone Analytics Suite", layout="wide")
st.title("AI Capstone Full-Stack Analytics Dashboard")
st.markdown("Exposing layout-aware NLP Parsers and Computer Vision Classifiers via high-speed FastAPI endpoints.")

col1, col2 = st.columns(2)

with col1:
    st.header("PDF Resume Analyzer Track")
    resume_file = st.file_uploader("Upload candidate resume document:", type=["pdf"])

    if st.button("Execute Resume Scan"):
        if resume_file is not None:
            files = {"file": (resume_file.name, resume_file.getvalue(), "application/pdf")}

            with st.spinner("Processing document data via NLP pipelines..."):
                response = requests.post("http://127.0.0.1:8000/analyze-resume", files=files)

            if response.status_code == 200:
                data = response.json()
                st.success("Analysis Complete!")
                st.metric(label="Predicted Track", value=data["predicted_category"])
                st.write("**Extracted Skill Matrix:**", data["extracted_skills"])
            else:
                st.error(f"Server Error: {response.json().get('detail', 'Unknown block issue')}")
        else:
            st.warning("Please attach a valid PDF document asset first.")

with col2:
    st.header("Computer Vision Face Tracker")
    image_file = st.file_uploader("Upload headshot profile media image:", type=["png", "jpg", "jpeg"])

    if st.button("Execute Image Scan"):
        if image_file is not None:
            mime_type = "image/png" if image_file.name.lower().endswith('.png') else "image/jpeg"
            files = {"file": (image_file.name, image_file.getvalue(), mime_type)}

            with st.spinner("Scanning matrix shapes via OpenCV classifiers..."):
                response = requests.post("http://127.0.0.1:8000/analyze-image", files=files)

            if response.status_code == 200:
                data = response.json()
                analysis = data["analysis"]
                st.success("Matrix Processing Complete!")
                st.metric(label="Face Detected", value=str(analysis["face_detected"]))
                st.metric(label="Total Facial Count Extraction", value=analysis["count"])
            else:
                st.error(f"Server Error: {response.json().get('detail', 'Unknown block issue')}")
        else:
            st.warning("Please attach a valid image media profile asset first.")