import time
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
st.title("This is a title")
st.header("this is a head")
st.subheader("this is a subheader")
st.text("this is a text")
st.markdown("# how's it look like - ok?")
''' 
# magic
1. first
2. second
'''
code = '''def hanshu():
... return 0
'''
st.code(code, language='python')
string1 = 'hello,*ok!*'
st.write(string1)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4, 5],
    'second column': [2, 3, 4, 5, 6],
}))
st.write('what', 1)
df = pd.DataFrame(
    np.random.randn(300, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c')
st.write(c)
if st.button('say it'):
    st.write('hello')
else:
    st.write('no?')
if st.checkbox('i agree'):
    st.write('you agree')
radio1 = st.radio('choose one', ['apple', 'orange', 'banana'])
if radio1 == 'apple':
    st.write('aaaaaa')
elif radio1 == 'orange':
    st.write('bbbbbb')
else:
    st.write('c')
opt = st.selectbox(
    'choose!',
    ('email', 'phone', 'mail'))
st.write('you anwser', opt)
opt2 = st.multiselect(
    'choose more than 1',
    ('blue', 'orange', 'what'))
st.write('your anwser2:', opt2)
x = st.slider('x is', 0, 100)
st.write('x +3 is', x+3)
title = st.text_input('shuru', 'sssssss')
st.write('ni input ', title)
jindu = st.slider('kongzhi jindutiao', 0, 100)
st.progress(jindu)
if st.button('jincheng'):
    with st.spinner('wait.....'):
        time.sleep(6)
    st.success('ok!')
else:
    st.write('dianji')
if st.button('qiqiu'):
    st.balloons()
md = st.text_input('input_to_md')
st.markdown(md)
