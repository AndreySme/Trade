import streamlit as st

high = float(st.text_input(label='Введите верхнюю цену'))
avr = float(st.text_input(label='Введите следующую цену'))
low = float(st.text_input(label='Введите нижнюю цену'))

result = high
st.write(result)

