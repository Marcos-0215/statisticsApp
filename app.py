import streamlit as st
from Data.grafic import plot_price

st.title('Histórico de Cotações')
st.write('Veja o histórico das cotações das empresas.')



#ticker = st.sidebar.text_input(
#    'Escolha o ticker:',
#    value = 'TSLA'
#    )


tickers_disponiveis = ['AAPL', 'AMZN', 'COST', 'DIS', 'GOOGL', 'MSFT', 'QQQ', 'TSLA', 'VT']

tickers = st.sidebar.multiselect(
    'Escolha os tickers:',
    options=tickers_disponiveis,
    default=['VT']
)


#fig = plot_price(ticker)
#st.plotly_chart(fig)

if tickers:
    for ticker in tickers:
        fig = plot_price(ticker)
        st.plotly_chart(fig)
else:
    st.write("Selecione pelo menos um ticker para visualizar o gráfico.")
