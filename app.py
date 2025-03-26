import streamlit as st
from Data.grafic import plot_price

st.title('Histórico de Cotações')
st.write('Veja o histórico das cotações das empresas.')


"""
ticker = st.sidebar.text_input(
    'Escolha o ticker:',
    value = ['TSLA', 'AAPL']
    )
"""

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






# Lista de opções disponíveis
tickers_disponiveis = ['TSLA', 'AAPL', 'MSFT', 'GOOGL', 'AMZN']

# Permite que o usuário selecione múltiplos tickers
tickers = st.sidebar.multiselect(
    'Escolha os tickers:',
    options=tickers_disponiveis,
    default=['TSLA']
)

# Gera e exibe os gráficos para cada ticker selecionado
if tickers:
    for ticker in tickers:
        fig = plot_price(ticker)
        st.plotly_chart(fig)
else:
    st.write("Selecione pelo menos um ticker para visualizar o gráfico.")
