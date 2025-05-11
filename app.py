import pandas as pd # pip install pandas openpyxl
import streamlit as st  # pip install streamlit
import plotly.express as px  # pip install plotly-express



# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
st.title("Sales Dashboard")
st.write("Welcome to the sales dashboard!")


# custom CSS
st.markdown("""
    <style>
    /* inset CSS to make the cursor a pointer on the dropdown arrow of multiselect/selectbox*/
    svg[title="open"] {
        cursor: pointer;
    }
    .st-emotion-cache-1xulwhk{font-size:1rem;}
    </style>
""", unsafe_allow_html=True)
# ---- READ EXCEL ----
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    # Add 'hour' column to dataframe
    #df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df
    print(df.head())

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

st.dataframe(df_selection)


# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.


# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI's
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("""---""")