import streamlit as st
import importlib
import os
import sys

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

def load_module(module_name):
    try:
        return importlib.import_module(module_name)
    except ImportError as e:
        st.error(f"Failed to import {module_name}: {str(e)}")
        return None

# Import the app modules
summary_app = load_module("summary.app")
compliance_app = load_module("compliance.app")
drafting_app = load_module("drafting.app")

def main():
    st.set_page_config(page_title="LegalSaathi Multi-App", layout="wide")

    st.title("Welcome to LegalSaathi")
    st.write("Choose a service to get started:")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Summary", "Compliance", "Drafting"])

    if selection == "Home":
        st.write("Please select a service from the sidebar to begin.")
    elif selection == "Summary":
        if summary_app:
            st.write("## Summary Service")
            summary_app.main()
        else:
            st.error("Summary service is currently unavailable.")
    elif selection == "Compliance":
        if compliance_app:
            st.write("## Compliance Service")
            compliance_app.main()
        else:
            st.error("Compliance service is currently unavailable.")
    elif selection == "Drafting":
        if drafting_app:
            st.write("## Drafting Service")
            drafting_app.main()
        else:
            st.error("Drafting service is currently unavailable.")

    st.sidebar.markdown("---")
    st.sidebar.write("© 2024 LegalSaathi. All rights reserved.")

if __name__ == "__main__":
    main()
