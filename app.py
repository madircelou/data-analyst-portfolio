import streamlit as st
import pandas as pd

st.title("My Data Analyst Portfolio")

st.header("About me")

st.write("""
Welcome to my data portfolio.
This dashboard showcases my analyses and experiments with data.
""")

st.header("Analyst metrics")

data = {
    "Metric": ["Datasets analysed", "SQL queries written", "Insights generated"],
    "Value": [12, 4300, 38]
}

df = pd.DataFrame(data)

st.table(df)

st.header("Vacation analytics")

travel_data = {
    "Year": [2021,2022,2023,2024],
    "Countries visited": [2,3,4,5]
}

travel_df = pd.DataFrame(travel_data)

st.line_chart(travel_df.set_index("Year"))
