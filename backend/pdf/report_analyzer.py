import re


def analyze_report(text):

    report = {}

    # -----------------------------
    # Patient Information
    # -----------------------------

    patterns = {
        "Patient Name": r"(?:Patient Name|Name)\s*[:\-]?\s*(.+)",
        "Age": r"Age\s*[:\-]?\s*(\d+)",
        "Gender": r"Gender\s*[:\-]?\s*(Male|Female|Other)",
        "Doctor": r"(?:Doctor|Dr\.?)\s*[:\-]?\s*(.+)",
        "Hospital": r"(?:Hospital|Clinic)\s*[:\-]?\s*(.+)",
        "Date": r"(?:Date|Report Date)\s*[:\-]?\s*([0-9/\-]+)"
    }

    for key, pattern in patterns.items():

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            report[key] = match.group(1).strip()
        else:
            report[key] = "Not Found"

    # -----------------------------
    # Medical Tests
    # -----------------------------

    tests = {
        "Hemoglobin": r"Hemoglobin\s*[:\-]?\s*([\d.]+)",
        "Glucose": r"(?:Glucose|Blood Sugar)\s*[:\-]?\s*([\d.]+)",
        "HbA1c": r"HbA1c\s*[:\-]?\s*([\d.]+)",
        "Cholesterol": r"Cholesterol\s*[:\-]?\s*([\d.]+)",
        "Vitamin D": r"Vitamin\s*D\s*[:\-]?\s*([\d.]+)",
        "Vitamin B12": r"Vitamin\s*B12\s*[:\-]?\s*([\d.]+)",
        "Creatinine": r"Creatinine\s*[:\-]?\s*([\d.]+)",
        "Urea": r"Urea\s*[:\-]?\s*([\d.]+)",
        "Platelets": r"Platelets\s*[:\-]?\s*([\d.]+)",
        "WBC": r"WBC\s*[:\-]?\s*([\d.]+)",
        "RBC": r"RBC\s*[:\-]?\s*([\d.]+)"
    }

    report["Tests"] = {}

    for test, pattern in tests.items():

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            report["Tests"][test] = match.group(1)

    return report