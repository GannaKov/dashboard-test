
import streamlit as st  # pip install streamlit
from openpyxl import load_workbook
from save_edited_data import save_edited_data  # Assuming this function is defined in save_edited_data.py
from get_data import get_data_from_excel

# ---- READ EXCEL ----

df = get_data_from_excel()
st.title("📋 Sales Data")
st.markdown("")
#st.dataframe(df.sort_values(by=['Date']), use_container_width=True)
# ---- EDIT DATA ----
# Uncomment the following lines to enable data editing and saving functionality
df= df.sort_values(by=['Date'])  # Sort by date for better readability
edited_df = st.data_editor(df)


if st.button("💾 Save Changes"):
    success, error = save_edited_data(edited_df)
    print("success", success)
    print("error", error)
    if success:
        st.cache_data.clear()  # Clear the cache to reflect changes
        st.success("Changes saved successfully!")
    else:
        st.error(f"Error saving file: {error}")

#   if st.button("💾 Save Changes"):
#      try:
#         # Save the edited data back to the Excel file
#         edited_df.to_excel("sales.xlsx", index=False, startrow=3)  # assuming headers start from row 4
#         st.success("Changes have been successfully saved to the file!")
#     except Exception as e:
#         st.error(f"An error occurred while saving: {e}") 