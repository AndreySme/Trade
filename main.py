import streamlit as st

high = st.text_input(label='Введите верхнюю цену')
avr = st.text_input(label='Введите следующую цену')
low = st.text_input(label='Введите нижнюю цену')
btn = st.button(label='Выполнить', on_click=True)
if btn:
  st.write(high)

st.write(type(result))

