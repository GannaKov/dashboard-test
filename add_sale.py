import streamlit as st  # pip install streamlit
import datetime
from append_data import append_data_to_excel 

st.html("./custom.css")

st.title("📋 Add Sale")
st.markdown("")
add_form = st.form('add_form ')
invoice_id= add_form.text_input("Invoice ID", "",max_chars =11,placeholder ="111-11-1111", help="Enter invoice ID")

branch = add_form.segmented_control(
    "Branch", ["A","B","C"], selection_mode="single", default ="A",  help="Select a branch"
)

city= add_form.selectbox(
    "City",
    ["Berlin", "Paris", "Rome", "Madrid", "Amsterdam", "Vienna", "Prague", "Lisbon"],
    help="Select a city",
)

customer_type =add_form.radio(
    "Customer Type",
    ["Member", "Normal"],
    horizontal=True, 
    help="Select customer type",
)
gender = add_form.radio("Gender", ["Female","Male","Other"], horizontal=True, help="Select gender")
product_line = add_form.selectbox(
    "Product Line",
    ["Health and beauty","Food and beverages", "Fashion accessories", "Electronic accessories", "Home and lifestyle", "Sports and travel"], help="Select a product line"
)

#--------------
age = add_form.number_input(
    "Age", value=None, placeholder="18", min_value=15, max_value=120, step=1, help="Enter age"
)


rating = add_form.number_input(
    "Rating", value=None, placeholder="10", min_value=0.0, max_value=10.0, step=0.1, help="Enter rating"
)

#----------------
payment = add_form.selectbox(
    "Payment method",
    ["Ewallet","Cash", "Credit Card", ],help="Select a payment method"
)
#----------------
today = datetime.datetime.now()
start_date = datetime.date(2022, 1, 1)
date = add_form.date_input("Date",value=today, min_value=start_date,max_value=today,  format="YYYY-MM-DD", help="Select a date")


container = add_form.container(border=True,key="time_container")
with container:
    st.write("Select time:")
    col1, col2 = st.columns(2)

    with col1:
        hour = st.selectbox("Hour", list(range(0, 24)), format_func=lambda x: f"{x:02}")

    with col2:
        minute = st.selectbox("Minute", list(range(0, 60)), format_func=lambda x: f"{x:02}")
time= f"{hour:02}:{minute:02}:00"  # Format the time as HH:MM:SS  
quantity = add_form.number_input(
    "Quantity", value=None, placeholder="5", min_value=1, max_value=40, step=1, help="Enter quantity"
)

price = add_form.number_input(
    "Unit price", value=None, placeholder="33.2", min_value=0.0, max_value=1000.0, step=0.1, help="Enter price"
)  
submit = add_form.form_submit_button('Add')
if_submit=False
if submit:
    # Check if all required fields are filled
    required_fields = [
        invoice_id, hour, minute, payment, date, gender,
        age, product_line, branch, city, customer_type,
        quantity, price, rating
    ]
    	

    if all(field is not None and field != "" for field in required_fields):
        if_submit=True
        
        tax = quantity * price * 0.05
        total = quantity * price + tax
        cogs = quantity * price
        margin_percent = 4.7619
        gross_income = total - cogs    
        data_to_add = {
            'Invoice ID': invoice_id,
            'Branch': branch,
            'City': city,

            'Customer_type': customer_type,
            "Gender": gender,
            "Age": age,

            "Rating": rating,
            "Product line": product_line,
            "Payment": payment,

            "Date": date,
            "Time": time,

            "Quantity": quantity,
            "Unit price": price,
            "Total": total,

            "Tax 5%": tax,
            "Cogs": cogs,
            "Gross margin percentage": margin_percent,
            "Gross income": gross_income,
            }
        success, error = append_data_to_excel(data_to_add )   
        if success:
           st.cache_data.clear()
           st.success("Data appended successfully! ✅")
        else:
           st.error(f"Error saving file: {error}")   
    else:
        st.warning("Please fill in all fields before submitting.")

st.write("Total: ", round(total , 4) if if_submit else "-")
st.write("Cogs: ", round(cogs, 4) if if_submit else "-")
st.write("Margin percent: ", round(margin_percent, 4) if if_submit else "-")
st.write("Gross income: ", round(gross_income, 4) if if_submit else "-")
st.write("Tax 5%: ", round(tax, 4) if if_submit else "-")

