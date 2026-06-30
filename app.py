import streamlit as st

from backend.database.models import initialize_database
from backend.utils.session_manager import (
    is_logged_in,
    logout,
)

from components.sidebar import show_sidebar

from components.login_ui import show as login_page
from components.register_ui import show as register_page
from components.dashboard_ui import show as dashboard_page
from components.upload_ui import show as upload_page
from components.chat_ui import show as chat_page
from components.history_ui import show as history_page

# ----------------------------------------------------
# Initialize Database
# ----------------------------------------------------

initialize_database()

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Healthcare Assistant",
    page_icon="🏥",
    layout="wide"
)

# ----------------------------------------------------
# Session Initialization
# ----------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Login"

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

show_sidebar()

# ----------------------------------------------------
# Authentication Pages
# ----------------------------------------------------

if not is_logged_in():

    if st.session_state.page == "Login":
        login_page()

    elif st.session_state.page == "Register":
        register_page()

    else:
        st.session_state.page = "Login"
        st.rerun()

# ----------------------------------------------------
# Logged-in Pages
# ----------------------------------------------------

else:

    page = st.session_state.page

    if page == "Dashboard":
        dashboard_page()

    elif page == "Upload":
        upload_page()

    elif page == "Chat":
        chat_page()

    elif page == "History":
        history_page()

    elif page == "Logout":
        logout()
        st.session_state.page = "Login"
        st.rerun()

    else:
        st.session_state.page = "Dashboard"
        st.rerun()