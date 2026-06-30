def validate_pdf(pdf_file):

    if pdf_file is None:
        return False, "Please upload a PDF."

    if not pdf_file.name.lower().endswith(".pdf"):
        return False, "Only PDF files are allowed."

    if pdf_file.size == 0:
        return False, "Uploaded PDF is empty."

    if pdf_file.size > 10 * 1024 * 1024:
        return False, "PDF size should be less than 10 MB."

    return True, "PDF validation successful."