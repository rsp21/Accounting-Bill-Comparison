# & "C:\Users\Pedro Sanhueza\AppData\Local\Programs\Python\Python313\Scripts\streamlit.cmd" run "c:/Users/Pedro Sanhueza/OneDrive - RSP Supply/Documents/Script/external projects/Brett Haws/Accounting-Bill-Comparison/streamlit-app/src/app.py"
# & "C:/Users/Pedro Sanhueza/AppData/Local/Programs/Python/Python313/Scripts/streamlit.exe" run "c:/Users/Pedro Sanhueza/OneDrive - RSP Supply/Documents/Script/external projects/Brett Haws/Accounting-Bill-Comparison/streamlit-app/src/app.py"

import streamlit as st
import pandas as pd
# import PyPDF2
import numpy as np
from utils.helpers import load_data, dataframe_matching, load_data_netsuite

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

col1, col2 = st.columns(2)

with col1:
    uploaded_file_1 = col1.file_uploader("Upload Manufactory file", type=["csv", "pdf"], key="file1")
    if uploaded_file_1:
        if uploaded_file_1.name.endswith('.csv'):
            try:
                df1 = load_data(uploaded_file_1)
                col1.subheader(uploaded_file_1.name)
                # col1.success("CSV file successfully uploaded and read.")
                col1.data_editor(df1, num_rows="dynamic")
            except Exception as e:
                col1.error(f"Error reading CSV: {e}")


with col2:
    df2 = load_data_netsuite()
    col2.subheader("NetSuite Data")
    col2.write('(automatically connected)')
    col2.data_editor(df2, num_rows="dynamic")

if not uploaded_file_1:
    st.stop()

# COMPARING

col1_m, col2_m = st.columns(2)

with col1_m:
    matching_column_manufactory = st.selectbox(
        f"Matching Column {uploaded_file_1.name}",
        ([x for x in df1.columns]),
    )

with col2_m:
    matching_column_netsuite = st.selectbox(
        f"Matching Column {uploaded_file_1.name}",
        ([x for x in df2.columns]),
    )

if st.button("Calculate Comparison", type="primary"):

    with st.spinner("Calculating..."):
    
        result = dataframe_matching(df1,df2,matching_column_manufactory,matching_column_netsuite)
        
        st.subheader("Missmatches")
        st.data_editor(result, num_rows="dynamic", key="results")
        
        csv = result.to_csv(index=False)
        st.download_button(
            label="📥 Download Results",
            data=csv,
            file_name="comparison_results.csv",
            mime="text/csv"
        )

# & "C:\Users\Pedro Sanhueza\AppData\Local\Programs\Python\Python313\Scripts\streamlit.cmd" run "c:/Users/Pedro Sanhueza/OneDrive - RSP Supply/Documents/Script/external projects/Brett Haws/Accounting-Bill-Comparison/streamlit-app/src/app.py"