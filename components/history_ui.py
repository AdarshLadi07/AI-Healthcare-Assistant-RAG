import streamlit as st

from backend.database.queries import get_chat_history


def show():

    st.title("📜 Chat History")

    st.divider()

    history = get_chat_history(
        st.session_state.user["email"]
    )

    if len(history) == 0:

        st.info("No chat history found.")

        return

    for question, answer, date in history:

        with st.expander(date):

            st.markdown("### 🙋 Question")

            st.write(question)

            st.markdown("### 🤖 Answer")

            st.write(answer)