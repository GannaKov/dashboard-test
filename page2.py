import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import plotly.express as px  # pip install plotly-express
from data import get_data_from_excel

# ---- READ EXCEL ----
df = get_data_from_excel()

st.html("./custom.css")


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


df_selection = df.query(
    "City == @city & Customer_type ==@customer_type & Gender == @gender"
)

# ---- PAGE ----
st.title("📈 Users Dashboard")
st.markdown("")
st.subheader("Overall Distribution")

# pie chart Gender
gender_counts = df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']


fig_gender = px.pie(gender_counts, names='Gender', values='Count', title='Gender Distribution',color='Gender',
             color_discrete_map={'Male':'royalblue',
                                 'Female':'tomato',
                                 'Other':'green'})
#st.plotly_chart(fig_gender)

# pie chart Sity
city_counts = df['City'].value_counts().reset_index()
city_counts.columns = ['City', 'Count']
fig_city = px.pie(city_counts, names='City', values='Count', title='City Distribution',)
#st.plotly_chart(fig_city)

# pie chart Customer_type
customer_type_counts = df['Customer_type'].value_counts().reset_index()
customer_type_counts.columns = ['Type', 'Count']
fig_customer_type = px.pie(customer_type_counts, names='Type', values='Count', title='Customer Type Distribution', color_discrete_sequence=px.colors.qualitative.Dark2)
#st.plotly_chart(fig_customer_type)

# pie chart Age
bins = [9, 19, 29, 39, 49, 59, 69]
labels = ['10-19', '20-29', '30-39', '40-49', '50-59', '60-69']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
age_group_counts = df['Age Group'].value_counts().sort_index().reset_index()
age_group_counts.columns = ['Age Group', 'Count']
fig_age = px.pie(
    age_group_counts,
    names='Age Group',
    values='Count',
    title='Age Group Distribution',
    color_discrete_sequence=px.colors.qualitative.Bold
)
#st.plotly_chart(fig_age)





first_column, second_column,third_column , = st.columns(3,gap="medium")
first_column.plotly_chart(fig_gender, use_container_width=True)
second_column.plotly_chart(fig_age, use_container_width=True)
third_column.plotly_chart(fig_customer_type, use_container_width=True)
#fourth
st.plotly_chart(fig_city)
st.markdown("""---""") 
#-----------------------
#-----------------------


