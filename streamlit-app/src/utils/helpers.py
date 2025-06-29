import pandas as pd
import streamlit as st
import requests
from io import StringIO
import time

@st.cache_data
def load_data(file):
    """
    Load and cache CSV data
    """
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def dataframe_matching(df1,df2,matching_column_manufactory,matching_column_netsuite):
    """
    Match tables based on their key column
    """
    try:

        # Define your matching columns
        matching_column_manufactory # column in df1
        matching_column_netsuite # column in df2

        # Optional: rename NetSuite column to match Manufactory for comparison
        df2_renamed = df2.rename(columns={matching_column_netsuite: matching_column_manufactory})

        # Find values in df1 not in df2
        df1_not_in_df2 = df1[~df1[matching_column_manufactory].isin(df2_renamed[matching_column_manufactory])]

        # Find values in df2 not in df1
        df2_not_in_df1 = df2_renamed[~df2_renamed[matching_column_manufactory].isin(df1[matching_column_manufactory])]

        # Find values in df2 that are in df1
        df2_in_df1 = df2_renamed[df2_renamed[matching_column_manufactory].isin(df1[matching_column_manufactory])]

        return df1_not_in_df2, df2_not_in_df1, df2_in_df1

    except Exception as e:
        st.error(f"Error in calculations: {e}")
        return None

def load_data_netsuite() -> pd.DataFrame:
    try:
        st.write('starting')
        url = 'https://5432914.app.netsuite.com/app/reporting/webquery.nl'
        params = {
            "compid": "5432914",
            "entity": "451563",
            "email": "brett.haws@rspsupply.com",
            "role": "1024",
            "cr": "615",
            "hash": "AAEJ7tMQl87BiU2hsYVm8At934P_K03JVaQPGUT5V-tfzMPzQsk"
        }
        response = requests.get(url,params=params)
        response.encoding = 'utf-8'  # or try 'utf-8-sig' if needed
        html_content = StringIO(response.text)
        df_table = pd.read_html(html_content, header=0)[0]

        try:
            st.write('return df_table')
            return df_table
        except Exception:
            st.write('cannot retrive table')
            pass

    except Exception as e:
        st.write(f"Data loading failed: {e}")

    return pd.DataFrame()