import pandas as pd
import streamlit as st
import requests
from io import StringIO

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

def perform_calculations(df1):
    """
    Perform comparison calculations between two dataframes
    """
    try:

        result = df1
        
        
        return result
    except Exception as e:
        st.error(f"Error in calculations: {e}")
        return None

def load_data_netsuite() -> pd.DataFrame:
    """
    Downloads and loads data from a NetSuite Web Query URL.
    Assumes the file is an Excel file unless proven otherwise.

    Parameters:
    - url (str): The full NetSuite Web Query URL.

    Returns:
    - pd.DataFrame: DataFrame containing the downloaded data.
    """
    try:
        url = 'https://5432914.app.netsuite.com/app/reporting/webquery.nl?compid=5432914&entity=451563&email=brett.haws@rspsupply.com&role=1024&cr=615&hash=AAEJ7tMQl87BiU2hsYVm8At934P_K03JVaQPGUT5V-tfzMPzQsk'
        response = requests.get(url)
        response.encoding = 'utf-8'  # or try 'utf-8-sig' if needed
        html_content = StringIO(response.text)
        df_table = pd.read_html(html_content, header=0)[0]

        try:
            return df_table
        except Exception:
            pass

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"Data loading failed: {e}")

    return pd.DataFrame()