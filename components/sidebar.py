import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("🏥 AI Healthcare")

        st.markdown("---")

        # Not logged in
        if not st.session_state.get("logged_in", False):

            if st.button("🔑 Login", use_container_width=True):
                st.session_state.page = "Login"
                st.rerun()

            if st.button("📝 Register", use_container_width=True):
                st.session_state.page = "Register"
                st.rerun()

            return

        # Logged in
        st.success(f"Welcome\n\n{st.session_state.get('user_name','User')}")

        st.markdown("---")

        if st.button("🏠 Dashboard", use_container_width=True):
            st.session_state.page = "Dashboard"
            st.rerun()

        if st.button("📤 Upload Report", use_container_width=True):
            st.session_state.page = "Upload"
            st.rerun()

        if st.button("💬 AI Chat", use_container_width=True):
            st.session_state.page = "Chat"
            st.rerun()

        if st.button("📜 History", use_container_width=True):
            st.session_state.page = "History"
            st.rerun()

        st.markdown("---")

        if st.button("🚪 Logout", use_container_width=True):

            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.session_state.page = "Login"

            st.rerun()