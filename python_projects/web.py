import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The Best Company")
st.write("Insert text here")
st.subheader("Our Team:")

col1, col2, col3 = st.columns(3)
df = pandas.read_csv("python_projects/data.csv")
with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        st.write(row["role"])
        st.image("python_projects/images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"]}')
        st.write(row["role"])
        st.image("python_projects/images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("python_projects/images/" + row["image"])