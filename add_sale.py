#import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
#import plotly.express as px  # pip install plotly-express
#from data import get_data_from_excel
st.html("./custom.css")

st.title("📋 Add Sale")
st.markdown("")
invoice_id= st.text_input("Invoice ID", "",max_chars =11,placeholder ="111-11-1111", help="Enter invoice ID")
st.write("The current movie title is", invoice_id)
branch = st.segmented_control(
    "Branch", ["A","B","C"], selection_mode="single", default ="A",  help="Select a branch"
)
st.markdown(f"Your selected options: {branch}.")
city= st.selectbox(
    "City",
    ["Berlin", "Paris", "Rome", "Madrid", "Amsterdam", "Vienna", "Prague", "Lisbon"],
    help="Select a city",
)
st.write("The current movie title is", city)
customer_type =st.radio(
    "Customer Type",
    ["Member", "Normal"],
    horizontal=True, 
    help="Select customer type",
)
gender = st.radio("Gender", ["Female","Male","Other"], horizontal=True, help="Select gender")
product_line = st.selectbox(
    "Product Line",
    ["Health and beauty","Food and beverages", "Fashion accessories", "Electronic accessories", "Home and lifestyle", "Sports and travel"], help="Select a product line"
)

#--------------
age=number = st.number_input(
    "Age", value=None, placeholder="18", min_value=15, max_value=120, step=1, help="Enter age"
)


rating=number = st.number_input(
    "Rating", value=None, placeholder="10", min_value=0.0, max_value=10.0, step=0.1, help="Enter rating"
)
# if selected is not None:
#     st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")

