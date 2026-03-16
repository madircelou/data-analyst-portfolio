import streamlit as st
import pandas as pd

st.title("Vacation Analytics")

data = {
    "Country":["Portugal","Italy","Spain"],
    "Satisfaction":[9,8,10]
}

df = pd.DataFrame(data)

st.bar_chart(df.set_index("Country"))
