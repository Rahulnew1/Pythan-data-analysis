import streamlit as st

st.title('sasta calculator')
st.write('this is a simple calcuation app')

c1,c2=st.columns(2)
c1.number_input('number 1', key='num1')
c2.number_input('number 2',key='num2')  

if st.button('add'):
    num1=st.session_state.num1
    num2=st.session_state.num2
    ans= num1 + num2
    st.info(f'{num1}+{num2}={ans}')
