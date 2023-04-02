import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Yusuf Abdur-Rasheed")
    content = """
    Hello, I am Yusuf! A beginner programmer who is 12 years old. I am situated in Solihull, England and go to Solihull
    School. I am experienced in HTML and CSS and learning python.
    """
    st.info(content)
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)