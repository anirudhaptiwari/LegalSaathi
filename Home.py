import streamlit as st
import importlib
import os

# Import the app modules
summary_app = importlib.import_module("summary.app")
compliance_app = importlib.import_module("compliance.app")
drafting_app = importlib.import_module("drafting.app")

def main():
    st.set_page_config(page_title="Multi-App Home", layout="wide")

    st.title("Welcome to Our Multi-App Service")
    st.write("Choose a service to get started:")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Summary", "Compliance", "Drafting"])

    if selection == "Home":
        st.write("Please select a service from the sidebar to begin.")
    elif selection == "Summary":
        st.write("## Summary Service")
        summary_app.main()
    elif selection == "Compliance":
        st.write("## Compliance Service")
        compliance_app.main()
    elif selection == "Drafting":
        st.write("## Drafting Service")
        drafting_app.main()

    st.sidebar.markdown("---")
    st.sidebar.write("© 2024 Your Company Name. All rights reserved.")

if __name__ == "__main__":
    main()
