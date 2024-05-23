import streamlit as st

high = st.text_input(label='Введите верхнюю цену')
avr = st.text_input(label='Введите следующую цену')
low = st.text_input(label='Введите нижнюю цену')

btn = st.button(label='Выполнить', type="primary")
result = high.float() + avr.float()
if btn:
    st.write(result)

