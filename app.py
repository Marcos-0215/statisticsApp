import streamlit as st
from Data.grafic import plot_price

st.title('Histórico de Cotações')
st.write('Veja o histórico das cotações das empresas.')

ticker = st.sidebar.text_input(
    'Escolha o ticker:',
    value = ['TSLA', 'AAPL']
    )
fig = plot_price(ticker)
st.plotly_chart(fig)