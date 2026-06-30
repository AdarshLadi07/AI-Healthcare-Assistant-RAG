An AI-powered Healthcare Assistant that analyzes medical reports, validates healthcare documents, and answers user questions using **Retrieval-Augmented Generation (RAG)** with **LangChain**, **Google Gemini**, and **FAISS**.

---

## 🚀 Features

- 👤 User Authentication (Login & Registration)
- 📄 Upload Medical Reports (PDF)
- ✅ Healthcare Document Validation
- 🧠 AI-Powered Medical Report Analysis
- 🔍 Retrieval-Augmented Generation (RAG)
- 💬 Chat with Your Medical Report
- 📚 Chat History Storage
- 🗂️ Vector Database using FAISS
- ⚡ Google Gemini Integration
- 🎨 Streamlit Interactive Dashboard

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI & LLM
- Google Gemini
- LangChain

### Vector Database
- FAISS

### Database
- SQLite

### PDF Processing
- PyMuPDF (fitz)

### Environment
- Python 3.11+

---

## 📂 Project Structure

```
AI-Healthcare-Assistant-v2/
│
├── backend/
│   ├── database/
│   ├── embeddings/
│   ├── llm/
│   ├── pdf/
│   ├── services/
│   ├── validators/
│   ├── vector_db/
│   └── utils/
│
├── components/
│
├── config/
│
├── assets/
│
├── uploads/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/AdarshLadi07/AI-Healthcare-Assistant-v2.git
```

### Move into the Project

```bash
cd AI-Healthcare-Assistant-v2
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧠 AI Workflow

1. User uploads a medical report.
2. PDF text is extracted.
3. Healthcare document is validated.
4. Text is split into chunks using LangChain.
5. Chunks are converted into embeddings.
6. Embeddings are stored in FAISS.
7. User asks questions.
8. Relevant chunks are retrieved.
9. Gemini generates context-aware answers.

## 📌 Future Enhancements

- Multi-language Support
- Voice Assistant
- OCR for Scanned Reports
- Medical Recommendation Engine
- Doctor Appointment Integration
- Cloud Database
- Docker Deployment

---

## 👨‍💻 Author

**Adarsh**

GitHub: https://github.com/AdarshLadi07

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
