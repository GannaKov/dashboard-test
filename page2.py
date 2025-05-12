import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import plotly.express as px  # pip install plotly-express
from data import get_data_from_excel

# ---- READ EXCEL ----
df = get_data_from_excel()

st.html("./custom.css")


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
fig_customer_type = px.pie(customer_type_counts, names='Type', values='Count', title='Customer Type Distribution')
#st.plotly_chart(fig_customer_type)

left_column, middle_column, right_column = st.columns(3,gap="medium")
left_column.plotly_chart(fig_gender, use_container_width=True)
middle_column.plotly_chart(fig_city, use_container_width=True)
right_column.plotly_chart(fig_customer_type, use_container_width=True)

st.markdown("""---""") 

