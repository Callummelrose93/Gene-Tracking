import streamlit as st
import pandas as pd



st.write("Hello, *World!* :sunglasses:")

st.write("This is my document **title**")


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]})
st.write(df)

x = 10 
st.write('x', x)
