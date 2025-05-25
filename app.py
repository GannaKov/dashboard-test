import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


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

main_page = st.Page("sales_overview.py", title="Sales Overview", icon="📊")
page_2 = st.Page("user_analytics.py", title="User Analytics", icon="📈")
page_3 = st.Page("view_data.py", title="Sales Data", icon="📋")
page_4 = st.Page("add_sale.py", title="Add Sale", icon="➕")

# Set up navigation
pg = st.navigation([main_page, page_2,page_3,page_4])
# Run the selected page
pg.run()
#-------------------












