import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import plotly.express as px  # pip install plotly-express
from get_data import get_data_from_excel
from distribution_charts import plot_distribution_pie
import datetime

# ---- READ EXCEL ----
df = get_data_from_excel()

st.html("./custom.css")


# for age group
# Create age groups
bins = [9, 19, 29, 39, 49, 59, 69]
labels = ['15-19', '20-29', '30-39', '40-49', '50-59', '60-69']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# ---- SIDEBAR ----

st.sidebar.header("Please Filter Here:")


# input city
options_city=df["City"].unique()

city =  st.sidebar.selectbox(
    "Select City:",
    (options_city),
   
)

# input customer type
options_customer_type=df["Customer_type"].unique()

customer_type = st.sidebar.selectbox(
    "Select Customer Type:",
    (options_customer_type),
   
)

#input gender
options_gender=df["Gender"].unique()

gender = st.sidebar.selectbox(
    "Select Gender:",
    (options_gender),
   
)

# input age group
options_age_group = df["Age Group"].cat.categories.tolist()

age_group = st.sidebar.selectbox(
    "Select Age Group:",
    (options_age_group),
   
   
)


# ---- PAGE ----
st.title("📈 User Analytics Dashboard")
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


df_selection = df.query(
    "Date >= @date_range[0] &  @date_range[1]>=Date  "
).copy()

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.


# GENERAL OVERVIEW
# TOP
st.subheader(f":blue[Report period: {date_range[0].strftime('%d.%m.%Y')} – {date_range[1].strftime('%d.%m.%Y')}]",divider=True)
st.subheader("General Overview")

# pie chart Gender
gender_counts = df_selection['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

fig_gender = px.pie(gender_counts, names='Gender', values='Count', title='Gender Distribution',color='Gender',
             color_discrete_map={'Male':'royalblue',
                                 'Female':'tomato',
                                 'Other':'green'})


# pie chart Sity
city_counts = df_selection['City'].value_counts().reset_index()
city_counts.columns = ['City', 'Count']

fig_city = px.pie(city_counts, names='City', values='Count', title='City Distribution',)


# pie chart Customer_type
customer_type_counts = df_selection['Customer_type'].value_counts().reset_index()
customer_type_counts.columns = ['Type', 'Count']

fig_customer_type = px.pie(customer_type_counts, names='Type', values='Count', title='Customer Type Distribution', color_discrete_sequence=px.colors.qualitative.Dark2)


# pie chart Age
age_group_counts = df_selection['Age Group'].value_counts().sort_index().reset_index()

age_group_counts.columns = ['Age Group', 'Count']
fig_age = px.pie(
    age_group_counts,
    names='Age Group',
    values='Count',
    title='Age Group Distribution',
    color_discrete_sequence=px.colors.qualitative.Bold
)


first_column, second_column,third_column , = st.columns(3,gap="small")
first_column.plotly_chart(fig_gender, use_container_width=True)
second_column.plotly_chart(fig_age, use_container_width=True)
third_column.plotly_chart(fig_customer_type, use_container_width=True)

#fourth chart
st.plotly_chart(fig_city)
st.markdown("""---""") 
#=======================================
#=======================================
#  BOTTOM

# Distribution in Age Group


st.subheader(f"Age Group Distribution")

# -------- Age By City-------
fig_age_by_city= plot_distribution_pie(
    df_selection,
    query_str="City == @city",
    query_vars={"city": city},
    distr_col="Age Group",
    label_name="Age Group",
    title_prefix="Age Group Distribution for ",
    color_set=px.colors.qualitative.Bold
)

#------------Age by customer Type---
fig_age_by_customer_type= plot_distribution_pie(
    df_selection,
    query_str="Customer_type ==@customer_type"   ,
    query_vars={"customer_type": customer_type},
    distr_col="Age Group",
    label_name="Age Group",
    title_prefix="Age Group Distribution for type ",
    color_set=px.colors.qualitative.Bold
)


#--------Age by Gender-------
fig_age_by_gender= plot_distribution_pie(
    df_selection,
    query_str="Gender == @gender"   ,
    query_vars={"gender": gender},
    distr_col="Age Group",
    label_name="Age Group",
    title_prefix="Age Group Distribution for ",
    color_set=px.colors.qualitative.Bold
)


first_age_column, second_age_column,third_age_column , = st.columns(3,gap="small")
first_age_column.plotly_chart(fig_age_by_city, use_container_width=True)
second_age_column.plotly_chart(fig_age_by_customer_type, use_container_width=True)
third_age_column.plotly_chart(fig_age_by_gender, use_container_width=True)
#=========================================


# Distribution in City

st.subheader(f"City Distribution")
# City By Age Group
fig_city_by_age = plot_distribution_pie(
    df_selection,
    query_str="`Age Group` == @age_group"  ,
    query_vars={"age_group": age_group},
    distr_col="City",
    label_name="City",
    title_prefix="City Distribution for ",
    color_set=px.colors.qualitative.Plotly
)

#------------City by customer Type---
fig_city_by_customer_type = plot_distribution_pie(
    df_selection,
    query_str="Customer_type ==@customer_type"  ,
    query_vars={"customer_type": customer_type},
    distr_col="City",
    label_name="City",
    title_prefix="City Distribution for type ",
    color_set=px.colors.qualitative.Plotly
)


#--------City by Gender-------
fig_city_by_gender= plot_distribution_pie(
    df_selection,
    query_str="Gender == @gender"   ,
    query_vars={"gender": gender},
    distr_col="City",
    label_name="City",
    title_prefix="City Distribution for ",
    color_set=px.colors.qualitative.Plotly
)


first_city_column, second_city_column,third_city_column  = st.columns(3,gap="small")
first_city_column.plotly_chart(fig_city_by_age, use_container_width=True)
second_city_column.plotly_chart(fig_city_by_customer_type, use_container_width=True)
third_city_column.plotly_chart(fig_city_by_gender, use_container_width=True)

#=========================================

# Distribution in Gender
st.subheader(f"Gender Distribution")

# Gender By City
fig_gender_by_city = plot_distribution_pie(
    df_selection,
    query_str="City == @city"  ,
    query_vars={"city": city},
    distr_col="Gender",
    label_name="Gender",
    title_prefix="Gender Distribution for ",
    color_set=px.colors.qualitative.Dark2
)

# Gender By Customer Type

fig_gender_by_customer_type = plot_distribution_pie(
    df_selection,
    query_str="Customer_type ==@customer_type"  ,
    query_vars={"customer_type": customer_type},
    distr_col="Gender",
    label_name="Gender",
    title_prefix="Gender Distribution for type ",
    color_set=px.colors.qualitative.Dark2
)


# Gender By Age Group
fig_gender_by_age= plot_distribution_pie(
    df_selection,
    query_str="`Age Group` == @age_group"  ,
    query_vars={"age_group": age_group},
    distr_col="Gender",
    label_name="Gender",
    title_prefix="Gender Distribution for ",
    color_set=px.colors.qualitative.Dark2
)

first_gender_column, second_gender_column,third_gender_column  = st.columns(3,gap="small")
first_gender_column.plotly_chart(fig_gender_by_age, use_container_width=True)
second_gender_column.plotly_chart(fig_gender_by_customer_type, use_container_width=True)
third_gender_column.plotly_chart(fig_gender_by_city, use_container_width=True)
#=========================================

# Distribution by Customer Type
st.subheader(f"Customer Type Distribution")

# Customer Type By City
fig_customer_type_by_city = plot_distribution_pie(
    df_selection,
    query_str="City == @city"  ,
    query_vars={"city": city},
    distr_col="Customer_type",
    label_name="Customer Type",
    title_prefix="Customer Type Distribution for ",
    color_set=px.colors.qualitative.Set1
)

# Customer Type By Age Group
fig_customer_type_by_age = plot_distribution_pie(
    df_selection,
    query_str="`Age Group` == @age_group" ,
    query_vars={"age_group": age_group},
    distr_col="Customer_type",
    label_name="Customer Type",
    title_prefix="Customer Type Distribution for ",
    color_set=px.colors.qualitative.Set1
)

# Customer Type By Gender
fig_customer_type_by_gender = plot_distribution_pie(
    df_selection,
    query_str="Gender == @gender",
    query_vars={"gender": gender},
    distr_col="Customer_type",
    label_name="Customer Type",
    title_prefix="Customer Type Distribution for ",
    color_set=px.colors.qualitative.Set1
)

first_customer_type_column, second_customer_type_column,third_customer_type_column  = st.columns(3,gap="small")
first_customer_type_column.plotly_chart(fig_customer_type_by_age, use_container_width=True)
second_customer_type_column.plotly_chart(fig_customer_type_by_gender, use_container_width=True)
third_customer_type_column.plotly_chart(fig_customer_type_by_city, use_container_width=True)
#=========================================

#df, query_str, query_vars, distr_col, label_name, title_prefix, color_set
fff = plot_distribution_pie(
    df_selection,
    query_str="Gender == @gender",
    query_vars={"gender": gender},
    distr_col="Customer_type",
    label_name="Customer Type",
    title_prefix="Customer Type Distribution for ",
    color_set=px.colors.qualitative.Set1
)

