import pandas as pd
import streamlit as st
import plotly_express as px

st.header('Análise de anuncio de vendas de veículos')

car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar Histograma') # criar um botao

if hist_button:
    st.write('Criando um histograma para o conjunto de daods de anúncio de carros.') # escrever uma mensagem

    fig = px.histogram(car_data, x="odometer") # criar histograma

    st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly interativo