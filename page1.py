import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit

import plotly.express as px  # pip install plotly-express
from data import get_data_from_excel


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/






# custom CSS

st.html("./custom.css")




# ---- READ EXCEL ----

df = get_data_from_excel()


# ---- SIDEBAR ----

st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
   
    default=df["City"].unique(),
    
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Gender"].unique(),
    
    #placeholder="Gender",
    #default=None,
    default=df["Gender"].unique(),
    
)

df_selection = df.query(
    "City == @city & Customer_type ==@customer_type & Gender == @gender"
)

#st.dataframe(df_selection)


# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.


# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("")

# TOP KPI's
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column,  right_column = st.columns(2)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with right_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")

st.markdown("")   

st.subheader(f"Average Sales Per Transaction:&nbsp;&nbsp;&nbsp;US $ {average_sale_by_transaction}")  

st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = df_selection.groupby(by=["Product line"])[["Total"]].sum().sort_values(by="Total")

fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)

# fig_product_sales.update_layout(
#     plot_bgcolor="rgba(0,0,0,0)",
#     xaxis=(dict(showgrid=False))
# )
#st.plotly_chart(fig_product_sales)

# SALES BY HOUR [BAR CHART]
sales_by_hour = df_selection.groupby(by=["hour"])[["Total"]].sum()

fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="<b>Sales by hour</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)

#st.plotly_chart(fig_hourly_sales)
left_column, right_column = st.columns(2, gap="medium")

left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)

#------------
gender_counts = df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

# Строим pie chart
fig = px.pie(gender_counts, names='Gender', values='Count', title='Gender Distribution',color='Gender',
             color_discrete_map={'Male':'royalblue',
                                 'Female':'tomato',
                                 'Other':'green'})
st.plotly_chart(fig)