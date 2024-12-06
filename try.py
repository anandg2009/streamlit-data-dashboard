# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# st.title("Simple Data Dashboard")

# # Upload CSV file
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# if uploaded_file is not None:
#     # Read the uploaded CSV file
#     df = pd.read_csv(uploaded_file)

#     # Clean column names (remove leading/trailing spaces)
#     df.columns = df.columns.str.strip()

#     st.subheader("Data Preview")
#     st.write(df.head())

#     st.subheader("Data Summary")
#     st.write(df.describe())

#     st.subheader("Filter Data")
#     columns = df.columns.tolist()

#     # Select column for filtering
#     selected_column = st.selectbox("Select column to filter by", columns)
#     unique_values = df[selected_column].dropna().unique()
#     selected_value = st.selectbox("Select value", unique_values)

#     # Filter the DataFrame
#     filtered_df = df[df[selected_column] == selected_value]
#     st.write(f"Filtered Data (by {selected_column} = {selected_value}):")
#     st.write(filtered_df)

#     st.subheader("Plot Data")

#     # Select columns for x and y axes
#     x_column = st.selectbox("Select x-axis column", columns, key="x_axis")
#     y_column = st.selectbox("Select y-axis column", columns, key="y_axis")

#     if st.button("Generate Plot"):
#         # Check if filtered data is not empty
#         if not filtered_df.empty:
#             # Validate that selected columns are present in the filtered DataFrame
#             if x_column in filtered_df.columns and y_column in filtered_df.columns:
#                 try:
#                     st.bar_chart(filtered_df.set_index(x_column)[y_column])
#                 except Exception as e:
#                     st.error(f"Error generating plot: {e}")
#             else:
#                 st.error("Selected columns for x-axis or y-axis are not present in the filtered data.")
#         else:
#             st.error("Filtered data is empty. Please adjust your filter criteria.")
# else:
#     st.info("Waiting for file upload...")
