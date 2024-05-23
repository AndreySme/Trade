import streamlit as st

def volume(high=0, intermediate=0, low=0, volume=0):
    # разница верхней цены и промежуточной цены
    diff_high_intermediate = high - between
    # 40% от разницы верхней цены и промежуточной цены
    diff_40 = diff_high_intermediate * 0.4
    # цена после усреднения
    avr = intermediate + diff_40
    # разница цены после усреднения и нижней цены
    diff_avr_low = avr - low
    # разница промежуточной цены и нижней цены
    diff_intermediate_low = intermediate - low
    # 40% от разницы промежуточной цены и нижней цены
    diff_intermediate_low_40 = diff_intermediate_low * 0.4
    # в этой цене мы хотим оказаться, 40% от нижней цены
    result = low + diff_intermediate_low_40
    # процент объема, на который необходимо совершить сделку по верхней и промежуточной ценам
    percent = diff_intermediate_low_40 / diff_avr_low
    # процент объема, на который необходимо совершить сделку по нижней цене
    percent_residue = 1 - percent
    # объем, на который необходимо совершить сделку по верхней и промежуточной ценам
    volume_percent = volume * percent
    # объем, на который необходимо совершить сделку по нижней цене
    volume_residue = volume - volume_percent
    # объем, на который необходимо совершить сделку по верхней цене
    volume_40_percent = volume_percent * 0.4
    # объем, на который необходимо совершить сделку по промежуточной цене
    volume_60_percent = volume - volume_40

    return volume_40_percent, volume_60_percent, volume_residue
    
    
high = st.text_input(label='Введите верхнюю цену')
intermediate = st.text_input(label='Введите промежуточную цену')
low = st.text_input(label='Введите нижнюю цену')
volume = st.text_input(label='Введите объем капитала')

btn = st.button(label='Выполнить', type="primary")


if btn:
    volume_high, volume_intermediate, volume_low = volume(high=float(high), 
                                                          intermediate=float(intermediate), 
                                                          low=float(low),
                                                          volume=float(volume))
    
    st.write(f"Первая покупка по", high, "на", volume_high)
    st.write("Вторая покупка по")
    st.write("Третья покупка по")

