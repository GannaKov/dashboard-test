import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import plotly.express as px  # pip install plotly-express
from data import get_data_from_excel
from distribution_charts import plot_distribution_pie

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

age_group = st.sidebar.selectbox(
    "Select Age Group:",
    (options_age_group),
   
   
)

# df_selection = df.query(
#     "City == @city & Customer_type ==@customer_type & Gender == @gender & `Age Group` == @age_group" 
# )

# ---- PAGE ----
st.title("📈 User Analytics Dashboard")
st.markdown("")
st.subheader("General Overview")

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


st.subheader(f"Age Group Distribution")
# Age By City
fig_age_by_city= plot_distribution_pie(
    df,
    query_str="City == @city",
    query_vars={"city": city},
    distr_col="Age Group",
    label_name="Age Group",
    title_prefix="Age Group Distribution for ",
    color_set=px.colors.qualitative.Bold
)

# df_selection_for_age_by_city = df.query(
#     "City == @city " 
# )

# age_group_counts_by_city = df_selection_for_age_by_city['Age Group'].value_counts().sort_index().reset_index()

# age_group_counts_by_city.columns = ['Age Group', 'Count'] 
# fig_age_by_city = px.pie(
#     age_group_counts_by_city,
#     names='Age Group',
#     values='Count',
#     title=f"Age Group Distribution for {city}",
#     color_discrete_sequence=px.colors.qualitative.Bold
# )

#------------Age by customer Type---
fig_age_by_customer_type= plot_distribution_pie(
    df,
    query_str="Customer_type ==@customer_type"   ,
    query_vars={"customer_type": customer_type},
    distr_col="Age Group",
    label_name="Age Group",
    title_prefix="Age Group Distribution for type ",
    color_set=px.colors.qualitative.Bold
)

# df_selection_for_age_by_customer_type = df.query(
#     "Customer_type ==@customer_type" 
# )

# age_group_counts_by_customer_type = df_selection_for_age_by_customer_type['Age Group'].value_counts().sort_index().reset_index()

# age_group_counts_by_customer_type.columns = ['Age Group', 'Count'] 
# fig_age_by_customer_type = px.pie(
#     age_group_counts_by_customer_type,
#     names='Age Group',
#     values='Count',
#     title=f'Age Group Distribution for type "{customer_type}"',
#     color_discrete_sequence=px.colors.qualitative.Bold
# )

#--------Age by Gender-------
fig_age_by_gender= plot_distribution_pie(
    df,
    query_str="Gender == @gender"   ,
    query_vars={"gender": gender},
    distr_col="Age Group",
    label_name="Age Group",
    title_prefix="Age Group Distribution for ",
    color_set=px.colors.qualitative.Bold
)


# df_selection_for_age_by_gender = df.query(
#     "Gender == @gender" 
# )

# age_group_counts_by_gender = df_selection_for_age_by_gender['Age Group'].value_counts().sort_index().reset_index()

# age_group_counts_by_gender.columns = ['Age Group', 'Count'] 
# fig_age_by_gender = px.pie(
#     age_group_counts_by_gender,
#     names='Age Group',
#     values='Count',
#     title=f"Age Group Distribution for {gender}",
#     color_discrete_sequence=px.colors.qualitative.Bold
# )


first_age_column, second_age_column,third_age_column , = st.columns(3,gap="small")
first_age_column.plotly_chart(fig_age_by_city, use_container_width=True)
second_age_column.plotly_chart(fig_age_by_customer_type, use_container_width=True)
third_age_column.plotly_chart(fig_age_by_gender, use_container_width=True)
#=========================================

# Distribution in City


st.subheader(f"City Distribution")
# City By Age Group
fig_city_by_age = plot_distribution_pie(
    df,
    query_str="`Age Group` == @age_group"  ,
    query_vars={"age_group": age_group},
    distr_col="City",
    label_name="City",
    title_prefix="City Distribution for ",
    color_set=px.colors.qualitative.Plotly
)
# df_selection_for_city_by_age = df.query(
#     "`Age Group` == @age_group" 
# )

# city_group_counts_by_age = df_selection_for_city_by_age['City'].value_counts().sort_index().reset_index()

# city_group_counts_by_age.columns = ['City', 'Count'] 
# fig_city_by_age = px.pie(
#     city_group_counts_by_age,
#     names='City',
#     values='Count',
#     title=f"City Distribution for {age_group}",
#     color_discrete_sequence=px.colors.qualitative.Plotly
# )
#st.plotly_chart(fig_city_by_age)

#------------City by customer Type---
fig_city_by_customer_type = plot_distribution_pie(
    df,
    query_str="Customer_type ==@customer_type"  ,
    query_vars={"customer_type": customer_type},
    distr_col="City",
    label_name="City",
    title_prefix="City Distribution for type ",
    color_set=px.colors.qualitative.Plotly
)

# df_selection_for_city_by_customer_type = df.query(
#     "Customer_type ==@customer_type" 
# )

# city_group_counts_by_customer_type = df_selection_for_city_by_customer_type['City'].value_counts().sort_index().reset_index()

# city_group_counts_by_customer_type.columns = ['City', 'Count']
# fig_city_by_customer_type = px.pie(
#     city_group_counts_by_customer_type,
#     names='City',
#     values='Count',
#     title=f'City Distribution for type "{customer_type}"',
#     color_discrete_sequence=px.colors.qualitative.Plotly
# )
#st.plotly_chart(fig_city_by_customer_type)

#--------City by Gender-------
fig_city_by_gender= plot_distribution_pie(
    df,
    query_str="Gender == @gender"   ,
    query_vars={"gender": gender},
    distr_col="City",
    label_name="City",
    title_prefix="City Distribution for ",
    color_set=px.colors.qualitative.Plotly
)

# df_selection_for_city_by_gender = df.query(
#     "Gender == @gender" 
# )

# city_group_counts_by_gender = df_selection_for_city_by_gender['City'].value_counts().sort_index().reset_index()

# city_group_counts_by_gender.columns = ['City', 'Count'] 
# fig_city_by_gender = px.pie(
#     city_group_counts_by_gender,
#     names='City',
#     values='Count',
#     title=f"City Distribution for {gender}",
#     color_discrete_sequence=px.colors.qualitative.Plotly
# )
#st.plotly_chart(fig_city_by_gender)

first_city_column, second_city_column,third_city_column  = st.columns(3,gap="small")
first_city_column.plotly_chart(fig_city_by_age, use_container_width=True)
second_city_column.plotly_chart(fig_city_by_customer_type, use_container_width=True)
third_city_column.plotly_chart(fig_city_by_gender, use_container_width=True)

#=========================================

# Distribution in Gender
st.subheader(f"Gender Distribution")

# Gender By City
fig_gender_by_city = plot_distribution_pie(
    df,
    query_str="City == @city"  ,
    query_vars={"city": city},
    distr_col="Gender",
    label_name="Gender",
    title_prefix="Gender Distribution for ",
    color_set=px.colors.qualitative.Dark2
)
# df_selection_for_gender_by_city = df.query(
#     "City == @city " 
# )

# gender_group_counts_by_city = df_selection_for_gender_by_city['Gender'].value_counts().sort_index().reset_index()

# gender_group_counts_by_city.columns = ['Gender', 'Count'] 
# fig_gender_by_city = px.pie(
#     gender_group_counts_by_city,
#     names='Gender',
#     values='Count',
#     title=f"Gender Distribution for {city}",
#     color_discrete_sequence=px.colors.qualitative.Dark2
# )
#st.plotly_chart(fig_gender_by_city)

# Gender By Customer Type

fig_gender_by_customer_type = plot_distribution_pie(
    df,
    query_str="Customer_type ==@customer_type"  ,
    query_vars={"customer_type": customer_type},
    distr_col="Gender",
    label_name="Gender",
    title_prefix="Gender Distribution for type ",
    color_set=px.colors.qualitative.Dark2
)
# df_selection_for_gender_by_customer_type = df.query(
#     "Customer_type ==@customer_type" 
# )

# gender_group_counts_by_customer_type = df_selection_for_gender_by_customer_type['Gender'].value_counts().sort_index().reset_index()

# gender_group_counts_by_customer_type.columns = ['Gender', 'Count']
# fig_gender_by_customer_type = px.pie(
#     gender_group_counts_by_customer_type,
#     names='Gender',
#     values='Count',
#     title=f'Gender Distribution for type "{customer_type}"',
#     color_discrete_sequence=px.colors.qualitative.Dark2
# )
#st.plotly_chart(fig_gender_by_customer_type)


# Gender By Age Group
fig_gender_by_age= plot_distribution_pie(
    df,
    query_str="`Age Group` == @age_group"  ,
    query_vars={"age_group": age_group},
    distr_col="Gender",
    label_name="Gender",
    title_prefix="Gender Distribution for ",
    color_set=px.colors.qualitative.Dark2
)
# df_selection_for_gender_by_age = df.query(
#     "`Age Group` == @age_group" 
# )

# gender_group_counts_by_age = df_selection_for_gender_by_age['Gender'].value_counts().sort_index().reset_index()

# gender_group_counts_by_age.columns = ['Gender', 'Count'] 
# fig_gender_by_age = px.pie(
#     gender_group_counts_by_age,
#     names='Gender',
#     values='Count',
#     title=f"Gender Distribution for {age_group}",
#     color_discrete_sequence=px.colors.qualitative.Dark2
# )
#st.plotly_chart(fig_gender_by_age)

first_gender_column, second_gender_column,third_gender_column  = st.columns(3,gap="small")
first_gender_column.plotly_chart(fig_gender_by_age, use_container_width=True)
second_gender_column.plotly_chart(fig_gender_by_customer_type, use_container_width=True)
third_gender_column.plotly_chart(fig_gender_by_city, use_container_width=True)
#=========================================

# Distribution by Customer Type
st.subheader(f"Customer Type Distribution")

# Customer Type By City
# df_selection_for_customer_type_by_city = df.query(
#     "City == @city" 
# )

# customer_type_group_counts_by_city = df_selection_for_customer_type_by_city['Customer_type'].value_counts().sort_index().reset_index()

# customer_type_group_counts_by_city.columns = ['Customer Type', 'Count'] 
# fig_customer_type_by_city = px.pie(
#     customer_type_group_counts_by_city,
#     names='Customer Type',
#     values='Count',
#     title=f"Customer Type Distribution for {city}",
#     color_discrete_sequence=px.colors.qualitative.Set1
# )
#st.plotly_chart(fig_customer_type_by_city)
fig_customer_type_by_city = plot_distribution_pie(
    df,
    query_str="City == @city"  ,
    query_vars={"city": city},
    distr_col="Customer_type",
    label_name="Customer Type",
    title_prefix="Customer Type Distribution for ",
    color_set=px.colors.qualitative.Set1
)

# Customer Type By Age Group

# df_selection_for_customer_type_by_age = df.query(
#     "`Age Group` == @age_group" 
# )

# customer_type_counts_by_age = df_selection_for_customer_type_by_age['Customer_type'].value_counts().sort_index().reset_index()

# customer_type_counts_by_age.columns = ['Customer Type', 'Count'] 
# fig_customer_type_by_age = px.pie(
#     customer_type_counts_by_age,
#     names='Customer Type',
#     values='Count',
#     title=f"Customer Type Distribution for {age_group}",
#     color_discrete_sequence=px.colors.qualitative.Set1
# )
#st.plotly_chart(fig_customer_type_by_age)
fig_customer_type_by_age = plot_distribution_pie(
    df,
    query_str="`Age Group` == @age_group" ,
    query_vars={"age_group": age_group},
    distr_col="Customer_type",
    label_name="Customer Type",
    title_prefix="Customer Type Distribution for ",
    color_set=px.colors.qualitative.Set1
)

# Customer Type By Gender
# df_selection_for_customer_type_by_gender = df.query(
#     "Gender == @gender" 
# )

# customer_type_group_counts_by_gender = df_selection_for_customer_type_by_gender['Customer_type'].value_counts().sort_index().reset_index()

# customer_type_group_counts_by_gender.columns = ['Customer Type', 'Count'] 
# fig_customer_type_by_gender = px.pie(
#     customer_type_group_counts_by_gender,
#     names='Customer Type',
#     values='Count',
#     title=f"Customer Type Distribution for {gender}",
#     color_discrete_sequence=px.colors.qualitative.Set1
# )
#st.plotly_chart(fig_customer_type_by_gender)
fig_customer_type_by_gender = plot_distribution_pie(
    df,
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
    df,
    query_str="Gender == @gender",
    query_vars={"gender": gender},
    distr_col="Customer_type",
    label_name="Customer Type",
    title_prefix="Customer Type Distribution for ",
    color_set=px.colors.qualitative.Set1
)

#st.plotly_chart(fff)