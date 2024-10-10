import streamlit as st
import sys
import os

# Add the compliance directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'compliance'))

# Import the main function from the compliance app
from app import main as compliance_main

if __name__ == "__main__":
    compliance_main()
