import streamlit as st


def is_logged_in():
    return st.session_state.get("logged_in", False)


def login(user):
    """
    Save logged-in user information.
    user is a dictionary returned by login_user()
    """

    st.session_state.logged_in = True
    st.session_state.user = user
    st.session_state.user_id = user["id"]
    st.session_state.user_name = user["name"]
    st.session_state.user_email = user["email"]
    st.session_state.user_role = user["role"]


def logout():
    st.session_state.clear()


def current_user():
    return st.session_state.get("user")