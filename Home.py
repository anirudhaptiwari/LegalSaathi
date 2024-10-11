import streamlit as st
import importlib
import os
import sys
import traceback

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
        st.sidebar.error(f"Traceback: {traceback.format_exc()}")
        return None

# Import the app modules
summary_app = load_module("summary.app")
compliance_app = load_module("compliance.app")
drafting_app = load_module("drafting.app")

def main():
    st.title("Welcome to LegalSaathi")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Home", "Summary", "Compliance", "Drafting"])
    st.sidebar.write(f"Current selection: {selection}")

    if selection == "Home":
        st.write("Choose a service to get started:")
        
        # Create three columns for better layout
        col1, col2, col3 = st.columns(3)
        
        # Summary Section
        with col1:
            st.write("### Summary")
            st.write("Get comprehensive summaries of legal documents")
            if st.button("Go to Summary"):
                selection = "Summary"
                run_subapp(summary_app, "Summary")
                
        # Compliance Section
        with col2:
            st.write("### Compliance")
            st.write("Check and ensure legal compliance")
            if st.button("Go to Compliance"):
                selection = "Compliance"
                run_subapp(compliance_app, "Compliance")
                
        # Drafting Section
        with col3:
            st.write("### Drafting")
            st.write("Draft legal documents with assistance")
            if st.button("Go to Drafting"):
                selection = "Drafting"
                run_subapp(drafting_app, "Drafting")
    
    # Handle navigation based on selection
    if selection == "Summary":
        run_subapp(summary_app, "Summary")
    elif selection == "Compliance":
        run_subapp(compliance_app, "Compliance")
    elif selection == "Drafting":
        run_subapp(drafting_app, "Drafting")

    st.sidebar.markdown("---")
    st.sidebar.write("© 2024 LegalSaathi. All rights reserved.")

def run_subapp(app_module, app_name):
    if app_module:
        st.write(f"## {app_name} Service")
        st.write(f"Attempting to run {app_name.lower()}_app.main()")
        try:
            # Check if the module has a main function
            if hasattr(app_module, 'main') and callable(app_module.main):
                app_module.main()
            else:
                st.error(f"{app_name} module does not have a valid main() function.")
        except Exception as e:
            st.error(f"Error in {app_name.lower()}_app.main(): {str(e)}")
            st.error(f"Traceback: {traceback.format_exc()}")
    else:
        st.error(f"{app_name} service is currently unavailable.")

if __name__ == "__main__":
    main()
