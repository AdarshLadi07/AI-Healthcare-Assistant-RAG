import fitz


def extract_text(pdf_file):

    pdf_file.seek(0)

    document = fitz.open(
        stream=pdf_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text