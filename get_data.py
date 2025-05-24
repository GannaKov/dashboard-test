# data.py
import pandas as pd
import streamlit as st

@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        # io="supermarkt_sales.xlsx",
        io="sales.xlsx",#!!!!!! then change to "supermarkt_sales.xlsx"
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:S",
        #nrows=1000,
    )
    df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d").dt.date
    df["Time"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.time
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    #df["month"] = pd.to_datetime(df["Date"], format="%Y-%m-%d").dt.month
    #df["year"] = pd.to_datetime(df["Date"], format="%Y-%m-%d").dt.year
    

    return df
