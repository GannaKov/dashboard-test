import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import plotly.express as px  # pip install plotly-express
from data import get_data_from_excel

# ---- READ EXCEL ----
df = get_data_from_excel()

st.html("./custom.css")

# for age group
# Create age groups
bins = [9, 19, 29, 39, 49, 59, 69]
labels = ['15-19', '20-29', '30-39', '40-49', '50-59', '60-69']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
#age_category=df['Age Group'].cat.categories.tolist()
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
#options_age_group=df["Age Group"].unique()[::-1] 

age_group = st.sidebar.selectbox(
    "Select Age Group:",
    (options_age_group),
   
   
)

# df_selection = df.query(
#     "City == @city & Customer_type ==@customer_type & Gender == @gender & `Age Group` == @age_group" 
# )

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





first_column, second_column,third_column , = st.columns(3,gap="small")
first_column.plotly_chart(fig_gender, use_container_width=True)
second_column.plotly_chart(fig_age, use_container_width=True)
third_column.plotly_chart(fig_customer_type, use_container_width=True)
#fourth
st.plotly_chart(fig_city)
st.markdown("""---""") 
#=======================================
#=======================================

# Distribution in Age Group
# By City

st.subheader(f"Distribution by Age Group")
df_selection_for_age_by_city = df.query(
    "City == @city " 
)

age_group_counts_by_city = df_selection_for_age_by_city['Age Group'].value_counts().sort_index().reset_index()

age_group_counts_by_city.columns = ['Age Group', 'Count'] #alreade done in the above code
fig_age_by_city = px.pie(
    age_group_counts_by_city,
    names='Age Group',
    values='Count',
    title=f"Distribution by Age Group in {city}",
    color_discrete_sequence=px.colors.qualitative.Bold
)

#------------Age by customer Type---

df_selection_for_age_by_customer_type = df.query(
    "Customer_type ==@customer_type" 
)

age_group_counts_by_customer_type = df_selection_for_age_by_customer_type['Age Group'].value_counts().sort_index().reset_index()

age_group_counts_by_customer_type.columns = ['Age Group', 'Count'] #alreade done in the above code
fig_age_by_customer_type = px.pie(
    age_group_counts_by_customer_type,
    names='Age Group',
    values='Count',
    title=f'Distribution by Age Group in type "{customer_type}"',
    color_discrete_sequence=px.colors.qualitative.Bold
)

#--------Gender-------

df_selection_for_age_by_gender = df.query(
    "Gender == @gender" 
)

age_group_counts_by_gender = df_selection_for_age_by_gender['Age Group'].value_counts().sort_index().reset_index()

age_group_counts_by_gender.columns = ['Age Group', 'Count'] 
fig_age_by_gender = px.pie(
    age_group_counts_by_gender,
    names='Age Group',
    values='Count',
    title=f"Distribution by Age Group for {gender}",
    color_discrete_sequence=px.colors.qualitative.Bold
)


first_age_column, second_age_column,third_age_column , = st.columns(3,gap="small")
first_age_column.plotly_chart(fig_age_by_city, use_container_width=True)
second_age_column.plotly_chart(fig_age_by_customer_type, use_container_width=True)
third_age_column.plotly_chart(fig_age_by_gender, use_container_width=True)
#=========================================
# df_selection_for_age = df.query(
#     "City == @city & Customer_type ==@customer_type & Gender == @gender " 
# )
# Distribution in City
# By Age Group

st.subheader(f"Distribution by City")
df_selection_for_city_by_age = df.query(
    "`Age Group` == @age_group" 
)

city_group_counts_by_age = df_selection_for_city_by_age['City'].value_counts().sort_index().reset_index()

city_group_counts_by_age.columns = ['City', 'Count'] #alreade done in the above code
fig_city_by_age = px.pie(
    city_group_counts_by_age,
    names='City',
    values='Count',
    title=f"Distribution by City in {age_group}",
    color_discrete_sequence=px.colors.qualitative.Plotly
)
#st.plotly_chart(fig_city_by_age)
#------------City by customer Type---

df_selection_for_city_by_customer_type = df.query(
    "Customer_type ==@customer_type" 
)

city_group_counts_by_customer_type = df_selection_for_city_by_customer_type['City'].value_counts().sort_index().reset_index()

city_group_counts_by_customer_type.columns = ['City', 'Count']
fig_city_by_customer_type = px.pie(
    city_group_counts_by_customer_type,
    names='City',
    values='Count',
    title=f'Distribution by City in type "{customer_type}"',
    color_discrete_sequence=px.colors.qualitative.Plotly
)
#st.plotly_chart(fig_city_by_customer_type)
#--------City by Gender-------

df_selection_for_city_by_gender = df.query(
    "Gender == @gender" 
)

city_group_counts_by_gender = df_selection_for_city_by_gender['City'].value_counts().sort_index().reset_index()

city_group_counts_by_gender.columns = ['City', 'Count'] 
fig_city_by_gender = px.pie(
    city_group_counts_by_gender,
    names='City',
    values='Count',
    title=f"Distribution by City for {gender}",
    color_discrete_sequence=px.colors.qualitative.Plotly
)
#st.plotly_chart(fig_city_by_gender)

first_city_column, second_city_column,third_city_column  = st.columns(3,gap="small")
first_city_column.plotly_chart(fig_city_by_age, use_container_width=True)
second_city_column.plotly_chart(fig_city_by_customer_type, use_container_width=True)
third_city_column.plotly_chart(fig_city_by_gender, use_container_width=True)

#=========================================
# df_selection_for_age = df.query(
#     "City == @city & Customer_type ==@customer_type & Gender == @gender " 
# )
# Distribution in Gender
st.subheader(f"Distribution by Gender")
# By City


# By Customer Type



# By Age Group

#=========================================
# df_selection_for_age = df.query(
#     "City == @city & Customer_type ==@customer_type & Gender == @gender " 
# )
# Distribution by Customer Type
st.subheader(f"Distribution by Customer Type")
# By City


# By Age Group



# By Gender
