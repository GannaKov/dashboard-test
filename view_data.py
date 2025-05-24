
import streamlit as st  # pip install streamlit


from get_data import get_data_from_excel

# ---- READ EXCEL ----

df = get_data_from_excel()
st.title("📋 Sales Data")
st.markdown("")
st.dataframe(df.sort_values(by=['Date']), use_container_width=True)
# ---- EDIT DATA ----
# Uncomment the following lines to enable data editing and saving functionality
""" edited_df = st.data_editor(df)
if st.button("💾 Save Changes"):
    try:
        # Save the edited data back to the Excel file
        edited_df.to_excel("sales.xlsx", index=False, startrow=3)  # assuming headers start from row 4
        st.success("Changes have been successfully saved to the file!")
    except Exception as e:
        st.error(f"An error occurred while saving: {e}") """