import streamlit as st
import numpy as np

high = st.text_input(label='Введите верхнюю цену')
avr = st.text_input(label='Введите следующую цену')
low = st.text_input(label='Введите нижнюю цену')

btn = st.button(label='Выполнить', type="primary")
result = np.astype(high, np.float32)
if btn:
    st.write(result)

