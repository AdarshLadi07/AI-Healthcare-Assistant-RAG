import os
import streamlit as st

from backend.validators.pdf_validator import validate_pdf
from backend.validators.medical_validator import validate_healthcare_document

from backend.pdf.pdf_loader import extract_text
from backend.pdf.report_analyzer import analyze_report

from backend.services.rag_pipeline import build_vector_database

UPLOAD_FOLDER = "uploads"


def show():

    st.title("📤 Upload Medical Report")

    st.divider()

    uploaded_file = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    if uploaded_file is None:
        st.info("Please upload a PDF document.")
        return

    # ------------------------------------------------
    # Validate PDF
    # ------------------------------------------------

    valid, message = validate_pdf(uploaded_file)

    if not valid:
        st.error(message)
        return

    st.success(message)

    # ------------------------------------------------
    # Save PDF
    # ------------------------------------------------

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    save_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(save_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success("PDF saved successfully.")

    # ------------------------------------------------
    # Extract Text
    # ------------------------------------------------

    with st.spinner("Extracting text from PDF..."):

        text = extract_text(uploaded_file)

    if len(text.strip()) == 0:
        st.error("Unable to extract text from PDF.")
        return

    # ------------------------------------------------
    # Validate Healthcare Content
    # ------------------------------------------------

    with st.spinner("Checking whether the document is healthcare related..."):

        result = validate_healthcare_document(text)

    if not result["related"]:

        st.error("❌ This document is NOT related to the Healthcare domain.")

        st.warning(result["reason"])

        return

    st.success("✅ Healthcare-related document verified.")

    st.info(result["reason"])

    # ------------------------------------------------
    # Build Vector Database
    # ------------------------------------------------

    try:

        with st.spinner("Building LangChain Vector Database..."):

            chunk_count = build_vector_database(text)

        st.success(
            f"✅ Vector Database Created ({chunk_count} Chunks)"
        )

    except Exception as e:

        st.error(f"Vector Database Error:\n{e}")

        return

    # ------------------------------------------------
    # Show Extracted Text
    # ------------------------------------------------

    st.divider()

    st.subheader("📄 Extracted Text")

    st.text_area(
        "Document Content",
        text,
        height=300
    )

    # ------------------------------------------------
    # Analyze Report
    # ------------------------------------------------

    report = analyze_report(text)

    st.divider()

    st.subheader("📋 Report Analysis")

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Patient Name:**", report.get("Patient Name", "N/A"))
        st.write("**Age:**", report.get("Age", "N/A"))
        st.write("**Gender:**", report.get("Gender", "N/A"))

    with col2:

        st.write("**Doctor:**", report.get("Doctor", "N/A"))
        st.write("**Hospital:**", report.get("Hospital", "N/A"))
        st.write("**Date:**", report.get("Date", "N/A"))

    # ------------------------------------------------
    # Medical Test Results
    # ------------------------------------------------

    st.divider()

    st.subheader("🩺 Medical Test Results")

    tests = report.get("Tests", [])

    if len(tests) == 0:

        st.warning("No medical test values found.")

    else:

        st.table(tests)

    # ------------------------------------------------
    # Save in Session
    # ------------------------------------------------

    st.session_state["report_text"] = text
    st.session_state["report_analysis"] = report

    st.success("✅ Report is ready for AI Chat.")