import plotly.express as px  # pip install plotly-express
import pandas as pd
import streamlit as st  # pip install streamlit
from data import get_data_from_excel


def plot_distribution_pie(df, query_str, query_vars, distr_col, label_name, title_prefix, color_set):
    """
Generates a pie chart showing the distribution of a selected column with optional filtering.

Example use case: Customer Type by Gender.
Parameters:
- df: DataFrame containing the data
- query_str: a string for df.query(), e.g. "Gender == @gender"
- query_vars: a dictionary of variables for query(), e.g. {"gender": "Male"}
- distr_col: the column to compute the distribution for (e.g. 'Customer_type')
- label_name: name to display on the chart for the distribution (e.g. 'Customer Type')
- title_prefix: text to appear before the filter value in the chart title (e.g. 'Customer Type Distribution for ')
- color_set: a Plotly color sequence to use for the chart
"""

    df_selection= df.query(
    query_str, local_dict=query_vars
    ) 

    # Group by the specified column and sum the values
    grouped_data = df_selection[distr_col].value_counts().sort_index().reset_index()
    grouped_data.columns = [label_name, 'Count']
    # Create a pie chart using Plotly Express
    suffix = list(query_vars.values())[0] if query_vars else ''
    fig = px.pie(
        grouped_data,
        names=label_name,
        values='Count',
        title=title_prefix+str(suffix),
        color_discrete_sequence=color_set,
        
    )
    return fig 

