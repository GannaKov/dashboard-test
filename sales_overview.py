import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import datetime
import plotly.express as px  # pip install plotly-express
from get_data import get_data_from_excel




# custom CSS

st.html("./custom.css")

# ---- READ EXCEL ----

df = get_data_from_excel()


# ---- SIDEBAR ----

st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select City:",
    options=df["City"].unique(),
   
    default=df["City"].unique(),
    
)

customer_type = st.sidebar.multiselect(
    "Select Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique(),
)

gender = st.sidebar.multiselect(
    "Select Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique(),
    
)
# -----Create df_selection ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("")

# ---- Date Filter ----
today = datetime.datetime.now().date()
start_date = datetime.date(2022, 1, 1)
date_range_form = st.form('date_range_form')

date_range_imput = date_range_form.date_input("Date range",[start_date ,today], min_value=start_date,max_value=today,  format="DD.MM.YYYY", help="Select date range")
submit = date_range_form.form_submit_button('Submit')
if len(date_range_imput) == 2 and date_range_imput[0] <= date_range_imput[1]:
   date_range=[date_range_imput[0], date_range_imput[1]]
else:
    st.warning("Please select a valid date range!") 
    date_range = [start_date, today]  


# ---- Filter DataFrame ----
# Filter the DataFrame based on the selections
df_selection = df.query(
    "City == @city & Customer_type ==@customer_type & Gender == @gender & Date >= @date_range[0] &  @date_range[1]>=Date  "
).copy()


# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.


# ---- MAINPAGE ----
# ----- TOP ------
# TOP 

st.subheader(f":blue[Report period: {date_range[0].strftime('%d.%m.%Y')} – {date_range[1].strftime('%d.%m.%Y')}]",divider=True)
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
#==========================================
#----- BOTTOM -----
# ---- Date Filter ----

# TOTAL BY Date [BAR CHART]
st.subheader("Total Sales by Month")
df_selection["Year_Month"] =pd.to_datetime(df_selection["Date"]).dt.to_period("M")
sales_by_month = df_selection.groupby(by=["Year_Month"])[["Total"]].sum().sort_values("Year_Month").reset_index()
sales_by_month["Year_Month"] = sales_by_month["Year_Month"].dt.strftime("%Y-%m") 

#with streamlit
st.bar_chart(
    sales_by_month,
    x="Year_Month",
    x_label ="Month-Year",
    y="Total",
    color="#43AD23",  
)

#=======================================
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


#=======================================
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


left_column, right_column = st.columns(2, gap="medium")

left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)

#=========================================================


