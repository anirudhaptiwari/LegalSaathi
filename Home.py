import streamlit as st
import subprocess
import os

def run_app(app_dir):
    subprocess.Popen(["streamlit", "run", os.path.join(app_dir, "app.py")])

def main():
    st.set_page_config(page_title="Multi-App Home", layout="wide")

    st.title("Welcome to Our Multi-App Service")
    st.write("Choose a service to get started:")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Summary Service"):
            run_app("1.summary")
            st.success("Summary app is running. Please check the new tab or window.")

    with col2:
        if st.button("Compliance Service"):
            run_app("2.compliance")
            st.success("Compliance app is running. Please check the new tab or window.")

    with col3:
        if st.button("Drafting Service"):
            run_app("3.drafting")
            st.success("Drafting app is running. Please check the new tab or window.")

    st.markdown("---")
    st.write("© 2024 Your Company Name. All rights reserved.")

if __name__ == "__main__":
    main()
