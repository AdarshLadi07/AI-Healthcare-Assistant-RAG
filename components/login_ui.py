import streamlit as st

from backend.auth.login import login_user
from backend.utils.session_manager import login


def show():

    st.title("🏥 AI Healthcare Assistant")

    st.subheader("Login")

    st.divider()

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):

        success, result = login_user(email, password)

        if success:

            login(result)

            st.success("Login Successful!")

            st.rerun()

        else:

            st.error(result)

    st.divider()

    if st.button("Create Account"):

        st.session_state.page = "Register"

        st.rerun()