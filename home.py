import streamlit as st
import pandas as pd 

st.title("🎇🎆Website Developing using Python🎆🎇")
st.header("🎈Website Developing using Python✨")

st.image('./img/รูปป.jpg')
st.subheader("❤Ananya Khiaohwan")

dt=pd.read_csv('./data/iris-3.csv')
st.header()
st.erite(dt.head(10))