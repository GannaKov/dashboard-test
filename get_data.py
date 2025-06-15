# data.py
import pandas as pd
import streamlit as st

@st.cache_data
def get_data_from_excel():
    try:
       df = pd.read_excel(
          # io="supermarkt_sales.xlsx",
          io="sales.xlsx",#!!!!!! then change to "supermarkt_sales.xlsx"
          engine="openpyxl",
          sheet_name="Sales",
          skiprows=3,
          usecols="B:S",
        )
       #check that file exists
    except FileNotFoundError:
        st.warning("⚠️ File 'sales.xlsx' not found. Please make sure the file is located in the project directory.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Error while reading the Excel file: {e}")
        return pd.DataFrame()
    
    try:
         df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d").dt.date
         df["Time"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.time
         df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    except Exception as e:
        st.error(f"❌ Error while processing date/time columns: {e}")
        return pd.DataFrame()
    

    return df
