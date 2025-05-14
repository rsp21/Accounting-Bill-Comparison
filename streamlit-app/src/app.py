import streamlit as st
import pandas as pd
import numpy as np
from utils.helpers import load_data, perform_calculations

def main():
    st.set_page_config(
        page_title="RSP Accounting Bill Comparison",
        page_icon="📊",
        layout="wide"
    )
    
    st.title("RSP Accounting Bill Comparison")
    
    # File uploaders
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Upload First CSV")
        file1 = st.file_uploader("Upload first CSV file", type=["csv"], key="file1")
        
    with col2:
        st.subheader("Upload Second CSV")
        file2 = st.file_uploader("Upload second CSV file", type=["csv"], key="file2")
    
    if file1 and file2:
        df1 = load_data(file1)
        df2 = load_data(file2)
        
        if df1 is not None and df2 is not None:
            st.subheader("Data Preview")
            
            tab1, tab2 = st.tabs(["First CSV", "Second CSV"])
            
            with tab1:
                st.dataframe(df1.head())
            
            with tab2:
                st.dataframe(df2.head())
            
            if st.button("Calculate Comparison", type="primary"):
                with st.spinner("Calculating..."):
                    result = perform_calculations(df1, df2)
                    
                    st.subheader("Results")
                    st.dataframe(result)
                    
                    csv = result.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results",
                        data=csv,
                        file_name="comparison_results.csv",
                        mime="text/csv"
                    )

if __name__ == "__main__":
    main()