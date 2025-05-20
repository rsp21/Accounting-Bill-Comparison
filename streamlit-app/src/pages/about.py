import streamlit as st
import PyPDF2

def show_about():
    st.title("About RSP Accounting Bill Comparison")
    
    st.markdown("""
    ### Purpose
    This application helps compare accounting bills by analyzing CSV files from different sources.
    
    ### How to Use
    1. Upload your first CSV file
    2. Upload your second CSV file
    3. Click Calculate to see the comparison
    4. Download results as needed
    
    ### Contact
    For support, please contact: support@example.com
    """)

if __name__ == "__main__":
    show_about()