import streamlit as st

high = st.text_input(label='Введите верхнюю цену')
avr = st.text_input(label='Введите следующую цену')
low = st.text_input(label='Введите нижнюю цену')

result = high
st.write(result)
st.write(type(result))

