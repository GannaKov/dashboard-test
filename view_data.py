import streamlit as st  # pip install streamlit
from save_edited_data import save_edited_data  
from get_data import get_data_from_excel

# ---- READ EXCEL ----

df = get_data_from_excel()
st.title("📋 Sales Data")
st.markdown("")

# ---- EDIT DATA ----
# data editing and saving functionality
df= df.sort_values(by=['Date'])  # Sort by date for better readability
edited_df = st.data_editor(df)


if st.button("💾 Save Changes"):
    success, error = save_edited_data(edited_df)
   
    if success:
        st.cache_data.clear()  # Clear the cache to reflect changes
        st.success("Changes saved successfully! 😍")
    else:
        st.error(f"Error saving file: {error}")

# prev ver
#   if st.button("💾 Save Changes"):
#      try:
#         # Save the edited data back to the Excel file
#         edited_df.to_excel("sales.xlsx", index=False, startrow=3)  # assuming headers start from row 4
#         st.success("Changes have been successfully saved to the file!")
#     except Exception as e:
#         st.error(f"An error occurred while saving: {e}") 