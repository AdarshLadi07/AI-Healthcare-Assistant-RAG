from backend.llm.gemini import model


def validate_healthcare_document(document_text):
    """
    Validate whether the uploaded PDF content is related
    to the healthcare/medical domain.

    Returns:
    {
        "related": True/False,
        "confidence": 100,
        "reason": "..."
    }
    """

    # Limit text sent to Gemini
    document_text = document_text[:6000]

    prompt = f"""
You are an expert Healthcare Document Classifier.

Your job is to determine whether the CONTENT of the uploaded document
belongs to the healthcare or medical domain.

IMPORTANT:
- Read ONLY the document content.
- Ignore the filename.
- Ignore the file extension.

Healthcare-related documents include:

• Blood Test Reports
• CBC Reports
• MRI Reports
• CT Scan Reports
• ECG Reports
• X-Ray Reports
• Ultrasound Reports
• Medical Prescriptions
• Hospital Reports
• Laboratory Reports
• Medical Certificates
• Patient Records
• Clinical Notes
• Doctor Notes
• Diagnostic Reports
• Healthcare Research Papers
• Disease Reports
• Pharmacy Reports

NOT healthcare-related documents include:

• Resume
• College Notes
• Programming Notes
• Operating Systems Notes
• Java Notes
• Python Notes
• Invoice
• Story Book
• Newspaper
• Finance Report
• Railway Ticket
• Legal Document
• Business Report

Reply ONLY in one of these formats.

If healthcare related:

RELATED
Reason: <one short sentence>

If not healthcare related:

NOT_RELATED
Reason: <one short sentence>

Document Content:

{document_text}
"""

    try:

        response = model.generate_content(prompt)

        answer = response.text.strip()

        if answer.upper().startswith("RELATED"):
            return {
                "related": True,
                "confidence": 100,
                "reason": answer
            }

        return {
            "related": False,
            "confidence": 100,
            "reason": answer
        }

    except Exception as e:

        return {
            "related": False,
            "confidence": 0,
            "reason": str(e)
        }