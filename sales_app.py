import streamlit as st
import pandas as pd

# Title and Subheader
st.title("Sales Summary App")
st.subheader("An interactive dashboard to view and filter sales data.")

# Task 1: Hardcoded DataFrame
data = {
    'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', 'Phone'],
    'Category': ['Electronics', 'Accessories', 'Electronics', 'Accessories', 'Electronics'],
    'Sales': [1200, 25, 300, 75, 800]
}
df = pd.DataFrame(data)

# Task 2: Sidebar Filter and Line Chart
# Adding the selectbox to the sidebar
category = st.sidebar.selectbox("Select a Category", df['Category'].unique())

# Filtering the data based on selection
filtered_df = df[df['Category'] == category]

# Main content area
st.write(f"Displaying sales for: **{category}**")
st.dataframe(filtered_df)

# Line chart of Sales values
st.line_chart(filtered_df['Sales'])
