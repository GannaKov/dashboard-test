

import pandas as pd
import streamlit as st
from openpyxl import load_workbook


def append_data_to_excel():
    file_path = 'sales.xlsx'
    sheet_name = 'Sales'
   
    
    
    
    df1 = pd.DataFrame({
            'Invoice ID': ['311-11-1111'],
            'Branch': ['A'],
            'City': ['Berlin'],
            'Customer Type': ['Member'],  }) 
    # load the existing workbook 
    workbook = load_workbook(file_path)
    worksheet = workbook[sheet_name]
    #get the last row in the worksheet
    start_row = 5
    #start_row = worksheet.max_row + 1 
    for row in range(5, worksheet.max_row + 2):
        if worksheet.cell(row=row, column=2).value is None:
            start_row = row
            break
    print("max_row",start_row)
    print("max",worksheet.max_row)
    workbook.close()
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        
        #writer.sheets = {ws.title: ws for ws in workbook.worksheets}
        df1.to_excel(
            writer,
            sheet_name=sheet_name, 
            index=False,
            header=False,         # don't write the header again
            startrow=start_row-1,# # start writing from the first row
            startcol=1            # Start writing from the first column B not A
        )
    
    st.success("Data appended successfully!")
    st.write("Data appended to Excel file.")

    
    
    

