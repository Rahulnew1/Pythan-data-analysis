import streamlit as st
import plotly.express as px
import numpy as np

st.title('MY FIRST APP IN STREAMLIT')
st.info('streamlit allow us to build app')
st.warning('this is a warning')

def fibonacci(start,stop):
    x=[start, start+1]
    for i in range (stop):
        x.append(x[-1]+x[-2])
    return x

start =st.slider('start',0,100,0)
stop=st.slider('stop',0,100,0)
data=np.array(fibonacci(start,stop))
sin=np.sin(data)
fig=px.area(y=data, x=sin)
st.plotly_chart(fig,use_container_width=True)