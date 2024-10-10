import streamlit as st
from streamlit_option_menu import option_menu
import time

st.set_page_config(
    page_title="Legal Saathi",
    page_icon="⚖️",
    layout="wide"
)

# Custom CSS with improved visibility and gradients
def local_css():
    st.markdown("""
        <style>
        .main {
            background: linear-gradient(135deg, #1a4a4a, #2a6b6b);
        }
        .css-1d391kg {
            background: linear-gradient(135deg, #1a4a4a, #2a6b6b);
        }
        .stButton>button {
            background: linear-gradient(45deg, #ff5722, #ff7043);
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 25px;
            border: none;
            transition: all 0.3s;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            box-shadow: 0 4px 15px rgba(255, 87, 34, 0.3);
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #ff7043, #ff5722);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(255, 87, 34, 0.4);
        }
        .service-card {
            background: linear-gradient(145deg, #ffffff, #f0f0f0);
            padding: 25px;
            border-radius: 15px;
            margin: 15px;
            transition: all 0.3s;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        }
        .service-card:hover {
            transform: translateY(-10px);
            box-shadow: 8px 8px 20px rgba(0,0,0,0.15);
        }
        .profile-card {
            background: linear-gradient(145deg, #ffffff, #f5f5f5);
            padding: 25px;
            border-radius: 15px;
            margin: 15px;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
            transition: all 0.3s;
        }
        .profile-card:hover {
            transform: translateY(-5px);
            box-shadow: 8px 8px 20px rgba(0,0,0,0.15);
        }
        h1 {
            color: #ffffff;
            font-size: 3.5rem;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            margin-bottom: 1rem;
        }
        h2 {
            color: #ffffff;
            font-size: 2.5rem;
            font-weight: bold;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        }
        h3 {
            color: #333333;
            font-size: 1.8rem;
            font-weight: bold;
        }
        p {
            color: #333333;
            font-size: 1.1rem;
            line-height: 1.6;
        }
        .hero-text {
            color: white;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
        }
        .gradient-header {
            background: linear-gradient(45deg, #1a4a4a, #2a6b6b);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
        }
        .animated-gradient {
            background: linear-gradient(-45deg, #1a4a4a, #2a6b6b, #3d8b8b, #2a6b6b);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .highlight-text {
            color: #ffffff;
            background: linear-gradient(45deg, #ff5722, #ff7043);
            padding: 0.5rem 1rem;
            border-radius: 5px;
            display: inline-block;
            margin: 0.5rem 0;
        }
        </style>
    """, unsafe_allow_html=True)

def navigate_to_service(service_name):
    # Update the query parameters
    st.query_params["page"] = service_name.lower()

def show_home():
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

def show_about():
    st.markdown("""
        <div class='gradient-header'>
            <h1 style='text-align: center;'>About Us</h1>
            <p style='color: white; text-align: center;'>
                At our core, we believe that positive thoughts fuel success and growth. With every challenge, 
                there is an opportunity, and with every setback, a chance to rise stronger.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center; color: #333;'>Our Team</h2>", unsafe_allow_html=True)
    
    team_members = [
        {
            "name": "Anirudha Tiwari",
            "role": "AI & Cybersecurity Expert",
            "description": "Specializes in applying advanced machine learning techniques to legal document automation."
        },
        {
            "name": "Ganesh Gangane",
            "role": "Technical Lead",
            "description": "Enhances the design and functionality of our AI-powered legal documentation assistant."
        },
        {
            "name": "Datta Bharde",
            "role": "NLP Specialist",
            "description": "Focuses on the development and refinement of models for legal language simplification."
        },
        {
            "name": "Omkar Shitole",
            "role": "ML Engineer",
            "description": "Develops intelligent algorithms for automated legal document drafting."
        }
    ]

    cols = st.columns(4)
    for col, member in zip(cols, team_members):
        with col:
            st.markdown(f"""
                <div class='profile-card'>
                    <img src='https://via.placeholder.com/100' style='border-radius: 50%; width: 100px; height: 100px; margin: 0 auto; display: block;'>
                    <h3 style='text-align: center; color: #ff5722; margin-top: 15px;'>{member['name']}</h3>
                    <p style='text-align: center; color: #666; font-weight: bold;'>{member['role']}</p>
                    <p style='text-align: justify; color: #333;'>{member['description']}</p>
                </div>
            """, unsafe_allow_html=True)

def show_contact():
    st.markdown("""
        <div class='gradient-header'>
            <h1 style='text-align: center;'>Contact Us</h1>
            <p style='color: white; text-align: center;'>Get in touch with our team</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background: white; padding: 25px; border-radius: 15px;'>
                <h3 style='color: #ff5722;'>Send us a message</h3>
        """, unsafe_allow_html=True)
        
        with st.form("contact_form"):
            st.text_input("Name", placeholder="Enter your name")
            st.text_input("Email", placeholder="Enter your email")
            st.text_area("Message", placeholder="Your message here")
            st.form_submit_button("Send Message", use_container_width=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background: white; padding: 25px; border-radius: 15px;'>
                <h3 style='color: #ff5722;'>Contact Information</h3>
                <p><b>Email:</b> contact@legalsaathi.com</p>
                <p><b>Phone:</b> +91 1234567890</p>
                <p><b>Address:</b> Mumbai, Maharashtra, India</p>
                <div style='margin-top: 20px;'>
                    <h4 style='color: #ff5722;'>Office Hours</h4>
                    <p>Monday - Friday: 9:00 AM - 6:00 PM</p>
                    <p>Saturday: 9:00 AM - 1:00 PM</p>
                    <p>Sunday: Closed</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

def main():
    local_css()
    
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

    show_home()

if __name__ == "__main__":
    main()
