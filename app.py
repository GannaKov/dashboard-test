import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit

import plotly.express as px  # pip install plotly-express
from data import get_data_from_excel


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


df = get_data_from_excel()

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
# Set up navigation
pg = st.navigation([main_page, page_2,])
# Run the selected page
pg.run()
#-------------------












