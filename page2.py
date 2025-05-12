import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import plotly.express as px  # pip install plotly-express
from data import get_data_from_excel

# ---- READ EXCEL ----
df = get_data_from_excel()

st.html("./custom.css")
#@st.cache_data
st.markdown("# Page 2 🧑‍🤝‍🧑")
st.sidebar.markdown("# Page 2 ❄️")
