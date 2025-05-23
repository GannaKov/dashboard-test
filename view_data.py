
import streamlit as st  # pip install streamlit


from get_data import get_data_from_excel

# ---- READ EXCEL ----

df = get_data_from_excel()
st.title("📋 Sales Data")
st.markdown("")
st.dataframe(df, use_container_width=True)
