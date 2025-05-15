import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit

import plotly.express as px  # pip install plotly-express
from data import get_data_from_excel

#import numpy as np # I needed it for update exel file

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

#Read exel file
#df = get_data_from_excel()

#----------For update exel file----------------
# df = pd.read_excel("supermarkt_sales.xlsx", engine="openpyxl")

# df["Age"] = np.random.randint(18, 65, size=len(df))

# cities = ["Berlin", "Paris", "Rome", "Madrid", "Amsterdam", "Vienna", "Prague", "Lisbon"]
# df["City"] = np.random.choice(cities, size=len(df))

# date_range = pd.date_range(start="2022-01-01", end="2025-05-01", freq='D')
# df["Date"] = np.random.choice(date_range, size=len(df))


# df.to_excel("supermarkt_sales_updated.xlsx", index=False)

#--------------

# ---- SIDEBAR ----
LOGO_URL_LARGE="images/logo200.png"
LOGO_URL_SMALL="images/logo200.png"


st.logo(
    LOGO_URL_LARGE,
    size="large",
    link="https://streamlit.io/gallery",
    icon_image=LOGO_URL_SMALL,
)

#---Pages---
# Define the pages

main_page = st.Page("page1.py", title="Sales Overview", icon="📊")
page_2 = st.Page("page2.py", title="User Analytics", icon="📈")
page_3 = st.Page("view_data.py", title="Sales Data", icon="📋")
page_4 = st.Page("add_sale.py", title="Add Sale", icon="➕")
# Set up navigation
pg = st.navigation([main_page, page_2,page_3,page_4])
# Run the selected page
pg.run()
#-------------------












