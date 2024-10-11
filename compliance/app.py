import streamlit as st
import os
import sys
from dotenv import load_dotenv
from fpdf import FPDF

# Load environment variables
load_dotenv()

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm_integration import LLMIntegration
import document_processor

def generate_pdf(summary, balance_score, compliance_check, key_clauses, overall_assessment):
    pdf = FPDF()
    pdf.add_page()
    
    # Set title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Compliance Analysis Report", ln=True, align="C")
    
    # Summary
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Summary", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(200, 10, summary)

    # Balance Score
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Balance Score", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, f"The contract balance score is: {balance_score}", ln=True)

    # Compliance Check
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Compliance Check", ln=True)
    for law, details in compliance_check.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, f"{law}", ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.cell(200, 10, f"Compliant: {details['compliant']}", ln=True)
        if details['issues']:
            pdf.multi_cell(200, 10, "Issues:")
            for issue in details['issues']:
                pdf.multi_cell(200, 10, f"- {issue}")
        else:
            pdf.multi_cell(200, 10, "No compliance issues found.")
        pdf.cell(200, 10, "---", ln=True)

    # Key Clauses
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Key Clauses", ln=True)
    if key_clauses:
        for clause in key_clauses:
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, f"Clause Type: {clause['type']}", ln=True)
            pdf.set_font("Arial", "", 12)
            pdf.multi_cell(200, 10, f"Content: {clause['content']}")
            pdf.multi_cell(200, 10, f"Analysis: {clause['analysis']}")
            if clause['issues']:
                pdf.multi_cell(200, 10, "Issues:")
                for issue in clause['issues']:
                    pdf.multi_cell(200, 10, f"- {issue}")
            else:
                pdf.multi_cell(200, 10, "No issues found.")
            pdf.cell(200, 10, "---", ln=True)
    else:
        pdf.multi_cell(200, 10, "No key clauses found.")

    # Overall Assessment
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, "Overall Assessment", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(200, 10, overall_assessment)

    return pdf

def main():
    st.title("Compliance Checker")

    # Get API key from environment variable or let user input it
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        if not api_key:
            st.warning("Please enter a valid API key to proceed.")
            return

    # Streamlit file uploader widget
    uploaded_file = st.file_uploader("Upload a contract file", type=['pdf', 'docx'])

    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Save the uploaded file temporarily
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract text from the uploaded document
        try:
            document_text = document_processor.process_document(uploaded_file.name)
        except Exception as e:
            st.error(f"Failed to process document: {e}")
            document_text = None

        if document_text:
            # Instantiate the LLM integration class
            llm = LLMIntegration(api_key=api_key)

            # Analyze the contract
            try:
                analysis = llm.analyze_contract(document_text)
            except Exception as e:
                st.error(f"Failed to analyze the contract: {e}")
                analysis = None

            if analysis is None:
                st.error("Failed to analyze the contract. Please check your API key and try again.")
            else:
                # Safely access elements of analysis
                try:
                    summary = analysis.get('summary', 'No summary available.')
                    balance_score = analysis.get('balance_score', 'N/A')
                    compliance_check = analysis.get('compliance_check', {})
                    key_clauses = analysis.get('key_clauses', [])
                    overall_assessment = analysis.get('overall_assessment', 'No overall assessment available.')

                    # Display the results in the Streamlit app
                    st.header("Compliance Analysis")

                    # Display Contract Summary
                    st.subheader("Summary")
                    st.write(summary)

                    # Display Balance Score
                    st.subheader("Balance Score")
                    st.write(f"The contract balance score is: {balance_score}")

                    # Display Compliance Check
                    st.subheader("Compliance Check")
                    for law, details in compliance_check.items():
                        st.write(f"**{law}**")
                        st.write(f"Compliant: {details['compliant']}")
                        if details['issues']:
                            st.write("Issues:")
                            for issue in details['issues']:
                                st.write(f"- {issue}")
                        else:
                            st.write("No compliance issues found.")
                        st.write("---")

                    # Display Key Clauses
                    st.subheader("Key Clauses")
                    if key_clauses:
                        for clause in key_clauses:
                            st.write(f"**Clause Type: {clause['type']}**")
                            st.write(f"Content: {clause['content']}")
                            st.write(f"Analysis: {clause['analysis']}")
                            if clause['issues']:
                                st.write("Issues:")
                                for issue in clause['issues']:
                                    st.write(f"- {issue}")
                            else:
                                st.write("No issues found.")
                            st.write("---")
                    else:
                        st.write("No key clauses found.")

                    # Display Overall Assessment
                    st.subheader("Overall Assessment")
                    st.write(overall_assessment)

                    # Button to download PDF
                    if st.button("Download PDF Report"):
                        pdf = generate_pdf(summary, balance_score, compliance_check, key_clauses, overall_assessment)
                        pdf_output = f"{uploaded_file.name}_compliance_report.pdf"
                        pdf.output(pdf_output)

                        with open(pdf_output, "rb") as f:
                            st.download_button(label="Download PDF", data=f, file_name=pdf_output, mime="application/pdf")

                except Exception as e:
                    st.error(f"Error in processing analysis: {e}")

        # Clean up the temporary file
        if os.path.exists(uploaded_file.name):
            os.remove(uploaded_file.name)

if __name__ == "__main__":
    main()
