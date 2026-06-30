import streamlit as st


def show():

    st.title("🏥 Dashboard")

    st.success("Login Successful!")

    st.markdown("---")

    st.subheader("Welcome to AI Healthcare Assistant")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Reports Uploaded", 0)

    with col2:
        st.metric("Chats", 0)

    st.markdown("---")

    st.info(
        """
        Use the sidebar to:

        📤 Upload Medical Reports

        💬 Chat with AI

        📜 View History
        """
    )