#  & "C:/Users/Pedro Sanhueza/AppData/Local/Programs/Python/Python313/Scripts/streamlit.exe" run "c:/Users/Pedro Sanhueza/OneDrive - RSP Supply/Documents/Script/external projects/Brett Haws/Accounting-Bill-Comparison/streamlit-app/src/app.py"

import streamlit as st
import pandas as pd
import PyPDF2
import numpy as np
from utils.helpers import load_data, perform_calculations, load_data_netsuite

st.set_page_config(
    page_title="RSP Accounting Bill Comparison",
    page_icon="📊",
    layout="wide" # "centered" or "wide"
)

st.title("RSP Accounting Bill Comparison")

# st.subheader("Please upload invoice CSV")

option = st.selectbox(
    "Company",
    ("Royal", "Company2", "Company3"),
    index=None,
    placeholder="Select contact method...",
)

uploaded_file = st.file_uploader("Upload first CSV file", type=["csv", "pdf"], key="file1")

if not uploaded_file:
    st.stop()

if uploaded_file is not None:
    file_name = uploaded_file.name
    file_type = file_name.split(".")[-1].lower()
    if file_type == "csv":
        try:
            df1 = load_data(uploaded_file)
            st.success("CSV file successfully uploaded and read.")
        except Exception as e:
            st.error(f"Error reading CSV: {e}")

    elif file_type == "pdf":
        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
            st.success("PDF file successfully uploaded and processed.")
            st.text_area("Extracted Text", text, height=300)
        except Exception as e:
            st.error(f"Error reading PDF: {e}")

    else:
        st.warning("Unsupported file type.")

    df2 = load_data_netsuite()

    if df1 is not None and df2 is not None:

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Invoice Data")
            st.data_editor(df1, num_rows="dynamic")
        with col2:
            st.subheader("NetSuite Data")
            st.data_editor(df2, num_rows="dynamic")

        if st.button("Calculate Comparison", type="primary"):
            with st.spinner("Calculating..."):
                result = perform_calculations(df1)
                
                st.subheader("Missmatches")
                st.data_editor(result, num_rows="dynamic")
                
                csv = result.to_csv(index=False)
                st.download_button(
                    label="📥 Download Results",
                    data=csv,
                    file_name="comparison_results.csv",
                    mime="text/csv"
                )