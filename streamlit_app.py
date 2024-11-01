import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 My new app!")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

df = pd.DataFrame({
    'first-column': [1,2,3,4],
    'second column': [10,20,30,40]
})

# static table
st.table(df)

st.title("This is a data frame")
dataframe = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(dataframe.style.highlight_max(axis=0));

st.title('Woo a map!')

map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)
st.write(map_data)

st.title('Wowie Widgets')

x = st.slider('Slide your age (?)') # this is a widget
st.write('You are', x, 'years old.')

if x >= 50:
    st.write('dang, your old asf')
elif x == 23:
    st.write('twinsies')

st.text_input("Your name", key="name")
input = st.session_state.name
st.write('Hello, ', input, '!')

with st.form('my_form'):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    submitted = st.form_submit_button("submit")
    if submitted:
        st.write('slider', slider_val, 'checkbox', checkbox_val)
st.write('Outside the from')