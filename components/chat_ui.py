import streamlit as st

from backend.services.rag_pipeline import ask_question
from backend.database.queries import save_chat


def show():

    st.title("💬 AI Healthcare Chat (RAG)")

    st.divider()

    if "report_text" not in st.session_state:

        st.warning("Please upload a medical report first.")

        return

    question = st.text_input(
        "Ask a question about your medical report"
    )

    if st.button("Ask AI", use_container_width=True):

        if question.strip() == "":

            st.warning("Please enter a question.")

            return

        with st.spinner("Searching medical report..."):

            answer = ask_question(question)

        try:

            save_chat(
                st.session_state.user["email"],
                question,
                answer
            )

        except Exception as e:

            st.warning(f"Chat could not be saved.\n{e}")

        st.success("Answer")

        st.write(answer)

    st.divider()

    st.info(
        """
### Example Questions

• What is my blood sugar?

• Is my cholesterol normal?

• Explain my HbA1c.

• Who is my doctor?

• Summarize my report.

• What are the abnormal values?

• Should I consult a doctor?
"""
    )