import streamlit as st
from PIL import Image
import base64
from streamlit_option_menu import option_menu
import time
from streamlit.components import v1

# Set page configuration
st.set_page_config(
    page_title="Legal Saathi",
    page_icon="⚖️",
    layout="wide"
)

# Custom CSS remains the same as your original code
def local_css():
    st.markdown("""
        <style>
        # Your existing CSS styles here...
        </style>
    """, unsafe_allow_html=True)

def navigate_to_service(service_name):
    """
    Navigate to the appropriate service page using Streamlit's page system
    """
    service_urls = {
        "Simplification": "https://legalsaathi-summary.streamlit.app",
        "Compliance": "https://legalsaathi-compliance.streamlit.app",
        "Drafting": "https://legalsaathi-drafting.streamlit.app"
    }
    
    if service_name in service_urls:
        st.markdown(f'<meta http-equiv="refresh" content="0;url={service_urls[service_name]}">', unsafe_allow_html=True)
        st.markdown(f"""
            <div style='padding: 20px; background-color: #f0f2f6; border-radius: 10px; text-align: center;'>
                <p>Redirecting to {service_name} service...</p>
                <p>Click <a href="{service_urls[service_name]}" target="_blank">here</a> if you are not redirected automatically.</p>
            </div>
        """, unsafe_allow_html=True)

def show_home():
    # Your existing show_home code remains the same until the button section
    st.markdown("""
        <div class='animated-gradient' style='padding: 50px; border-radius: 15px; text-align: center;'>
            <h1>Legal Saathi</h1>
            <h3 class='hero-text'>AI Powered Legal Document Assistant</h3>
            <p class='hero-text' style='max-width: 800px; margin: 20px auto; font-size: 1.2rem;'>
                <b>"Our AI-driven legal assistant simplifies complex legal documents, making them more accessible to individuals and small businesses. 
                By utilizing advanced natural language processing, we generate bilingual legal documents that are clear, compliant, 
                and tailored to the Indian legal framework."</b>
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    cols = st.columns(3)
    
    services = [
        {
            "title": "Simplification",
            "description": "Transform complex legal documents into easy-to-understand language using our AI-powered simplification tool."
        },
        {
            "title": "Compliance",
            "description": "Ensure your legal documents meet all regulatory requirements with our automated compliance checker."
        },
        {
            "title": "Drafting",
            "description": "Generate professional legal documents tailored to your specific needs with our AI drafting assistant."
        }
    ]

    for col, service in zip(cols, services):
        with col:
            st.markdown(f"""
                <div class='service-card'>
                    <h3 style='text-align: center; color: #ff5722;'>{service['title']}</h3>
                    <p style='text-align: justify; color: #333;'><b>{service['description']}</b></p>
                    <div style='text-align: center; margin-top: 15px;'>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Try {service['title']}", key=f"home_{service['title'].lower()}"):
                navigate_to_service(service['title'])

def show_services():
    # Your existing show_services code remains the same until the button section
    st.markdown("""
        <div class='gradient-header'>
            <h1 style='text-align: center;'>Our Services</h1>
            <p style='color: white; text-align: center;'>Comprehensive Legal Solutions Powered by AI</p>
        </div>
    """, unsafe_allow_html=True)
    
    services = [
        {
            "title": "Simplification",
            "description": "Transform complex legal jargon into easy-to-understand language using advanced NLP algorithms.",
            "icon": "🔍"
        },
        {
            "title": "Compliance",
            "description": "Ensure all documents adhere to relevant legal standards and regulations with our AI-powered verification system.",
            "icon": "✓"
        },
        {
            "title": "Drafting",
            "description": "Generate customized legal documents with our state-of-the-art AI system, tailored to your specific needs.",
            "icon": "📝"
        }
    ]
    
    cols = st.columns(3)
    for col, service in zip(cols, services):
        with col:
            st.markdown(f"""
                <div class='service-card'>
                    <div style='text-align: center; font-size: 3rem; margin-bottom: 15px;'>{service['icon']}</div>
                    <h3 style='text-align: center; color: #ff5722;'>{service['title']}</h3>
                    <p style='text-align: justify; color: #333;'>{service['description']}</p>
                </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Try {service['title']} Now", key=f"try_{service['title'].lower()}"):
                navigate_to_service(service['title'])

# show_about and show_contact functions remain the same as in your original code

def main():
    local_css()
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Services", "About", "Contact"],
        icons=["house-fill", "gear-fill", "info-circle-fill", "envelope-fill"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background": "linear-gradient(90deg, #1a4a4a, #2a6b6b)"},
            "icon": {"color": "white", "font-size": "25px"}, 
            "nav-link": {
                "color": "white",
                "font-size": "16px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#ff5722",
                "font-weight": "bold"
            },
            "nav-link-selected": {"background": "linear-gradient(90deg, #ff5722, #ff7043)"},
        }
    )

    with st.spinner("Loading..."):
        time.sleep(0.5)
        if selected == "Home":
            show_home()
        elif selected == "Services":
            show_services()
        elif selected == "About":
            show_about()
        elif selected == "Contact":
            show_contact()

if __name__ == "__main__":
    main()
