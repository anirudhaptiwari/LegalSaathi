import streamlit as st
import importlib
import os
import sys

# Set page config at the very beginning
st.set_page_config(page_title="LegalSaathi Multi-App", layout="wide")

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

def load_module(module_name):
    try:
        module = importlib.import_module(module_name)
        st.sidebar.success(f"Successfully imported {module_name}")
        return module
    except ImportError as e:
        st.sidebar.error(f"Failed to import {module_name}: {str(e)}")
        return None

# Import the app modules
summary_app = load_module("summary.app")
compliance_app = load_module("compliance.app")
drafting_app = load_module("drafting.app")

def main():
    st.title("Welcome to LegalSaathi")
    st.write("Choose a service to get started:")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Summary", "Compliance", "Drafting"])

    st.sidebar.write(f"Current selection: {selection}")

    if selection == "Home":
        st.write("Please select a service from the sidebar to begin.")
    elif selection == "Summary":
        if summary_app:
            st.write("## Summary Service")
            st.write("Attempting to run summary_app.main()")
            try:
                summary_app.main()
            except Exception as e:
                st.error(f"Error in summary_app.main(): {str(e)}")
        else:
            st.error("Summary service is currently unavailable.")
    elif selection == "Compliance":
        if compliance_app:
            st.write("## Compliance Service")
            st.write("Attempting to run compliance_app.main()")
            try:
                compliance_app.main()
            except Exception as e:
                st.error(f"Error in compliance_app.main(): {str(e)}")
        else:
            st.error("Compliance service is currently unavailable.")
    elif selection == "Drafting":
        if drafting_app:
            st.write("## Drafting Service")
            st.write("Attempting to run drafting_app.main()")
            try:
                drafting_app.main()
            except Exception as e:
                st.error(f"Error in drafting_app.main(): {str(e)}")
        else:
            st.error("Drafting service is currently unavailable.")

    st.sidebar.markdown("---")
    st.sidebar.write("© 2024 LegalSaathi. All rights reserved.")

if __name__ == "__main__":
    main()
