import streamlit as st
from Data.grafic import plot_price

st.title('Histórico de Cotações')
st.write('Veja o histórico das cotações das empresas.')



#ticker = st.sidebar.text_input(
#    'Escolha o ticker:',
#    value = 'TSLA'
#    )


tickers_disponiveis = ['TSLA', 'AAPL', 'MSFT', 'GOOGL', 'AMZN']

tickers = st.sidebar.multiselect(
    'Escolha os tickers:',
    options=tickers_disponiveis,
    default=['TSLA']
)


#fig = plot_price(ticker)
#st.plotly_chart(fig)

if tickers:
    for ticker in tickers:
        fig = plot_price(ticker)
        st.plotly_chart(fig)
else:
    st.write("Selecione pelo menos um ticker para visualizar o gráfico.")
