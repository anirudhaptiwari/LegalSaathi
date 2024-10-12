import streamlit as st
import importlib
import os
import sys
import traceback
from streamlit.web.server.websocket_headers import get_url_params

# Set page config at the very beginning
st.set_page_config(page_title="LegalSaathi Multi-App", layout="wide")

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

def load_module(module_name):
    try:
        module = importlib.import_module(module_name)
        return module
    except ImportError as e:
        st.error(f"Failed to import {module_name}: {str(e)}")
        st.error(f"Traceback: {traceback.format_exc()}")
        return None

# Import the app modules
summary_app = load_module("summary.app")
compliance_app = load_module("compliance.app")
drafting_app = load_module("drafting.app")

def main():
    st.title("Welcome to LegalSaathi")
    
    # Get the current page from URL parameters
    params = get_url_params()
    current_page = params.get("page", ["Home"])[0]

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    
    # Create navigation links
    if st.sidebar.button("Home"):
        st.experimental_set_query_params(page="Home")
        st.experimental_rerun()
    if st.sidebar.button("Summary"):
        st.experimental_set_query_params(page="Summary")
        st.experimental_rerun()
    if st.sidebar.button("Compliance"):
        st.experimental_set_query_params(page="Compliance")
        st.experimental_rerun()
    if st.sidebar.button("Drafting"):
        st.experimental_set_query_params(page="Drafting")
        st.experimental_rerun()

    # Display content based on the current page
    if current_page == "Home":
        st.write("Please select a service from the sidebar to begin.")
        
        # Display service descriptions on home page
        st.write("### Our Services:")
        st.write("**Summary**: Get comprehensive summaries of legal documents")
        st.write("**Compliance**: Check and ensure legal compliance")
        st.write("**Drafting**: Draft legal documents with assistance")
    
    elif current_page == "Summary":
        run_subapp(summary_app, "Summary")
    elif current_page == "Compliance":
        run_subapp(compliance_app, "Compliance")
    elif current_page == "Drafting":
        run_subapp(drafting_app, "Drafting")
    
    st.sidebar.markdown("---")
    st.sidebar.write("© 2024 LegalSaathi. All rights reserved.")

def run_subapp(app_module, app_name):
    if app_module:
        st.write(f"## {app_name} Service")
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
