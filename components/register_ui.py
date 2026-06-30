import streamlit as st

from backend.auth.register import register_user


def show():

    st.title("📝 Register")

    st.divider()

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm = st.text_input(
        "Confirm Password",
        type="password"
    )

    role = st.selectbox(
        "Role",
        [
            "Patient",
            "Doctor"
        ]
    )

    if st.button("Register", use_container_width=True):

        if password != confirm:

            st.error("Passwords do not match.")

        else:

            success, message = register_user(
                name,
                email,
                password,
                role
            )

            if success:

                st.success(message)

            else:

                st.error(message)

    st.write("---")

    if st.button("Back to Login"):

        st.session_state.page = "login"

        st.rerun()