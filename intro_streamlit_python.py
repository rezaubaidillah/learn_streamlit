import streamlit as st
import pandas as pd
#text
st.title('tittle') 
st.header('header')
st.subheader('subheader')
st.caption('caption Copyright (c) 2023')
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

st.markdown(
    """
    # markdown
    markdownmarkdownmarkdownmarkdownmarkdown
    """
)
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

st.text('texttexttexttexttext')

st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")
#data display
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
 
st.dataframe(data=df, width=500, height=150)

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
#chart
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

name = st.text_input(label='Nama lengkap', value='')
st.write('Nama: ', name)

text = st.text_area('Feedback')
st.write('Feedback: ', text)

number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')

import datetime

date = st.date_input(label='Tanggal lahir', min_value=datetime.date(1900, 1, 1))
st.write('Tanggal lahir:', date)

uploaded_file = st.file_uploader('Choose a CSV file')
 
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
    
    
picture = st.camera_input('Take a picture')
if picture:
    st.image(picture)
    
if st.button('Say hello'):
    st.write('Hello there')
    
agree = st.checkbox('I agree')
 
if agree:
    st.write('Welcome to MyApp')
    
genre = st.radio(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary'),
    horizontal=False
)

genre = st.selectbox(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

genre = st.multiselect(
    label="What's your favorite movie genre",
    options=('Comedy', 'Drama', 'Documentary')
)

values = st.slider(
    label='Select a range of values',
    min_value=0, max_value=100, value=(0))
st.write('Values:', values)