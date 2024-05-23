import streamlit as st

high = st.text_input(label='Введите верхнюю цену')
avr = st.text_input(label='Введите следующую цену')
low = st.text_input(label='Введите нижнюю цену')

btn = st.button(label='Выполнить', type="primary")
if btn:
    st.write(high+avr)

