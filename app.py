import pandas as pd
import streamlit as st
import plotly_express as px

st.header('Análise de anuncio de vendas de veículos') # título

car_data = pd.read_csv('vehicles.csv') # lendo os dados

hist_button = st.button('Criar Histograma') # criar um botao
dis_button = st.button('Criar gráfico de dispersão') # criar um botão


if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncio de carros.') # escrever uma mensagem

    fig = px.histogram(car_data, x="odometer") # criar histograma
    st.plotly_chart(fig, use_container_width=True) # exibir um gráfico Plotly interativo

if dis_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncio de carros.')

    fig1 = px.scatter(car_data, x="odometer", y="price")  # criar um gráfico de dispersão
    st.plotly_chart(fig1, use_container_width=True)  # exibir um gráfico Plotly interativo


# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')
build_dis = st.checkbox('Criar um gráfico de dispersão')

if build_histogram: # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')

    fig = px.histogram(car_data, x="odometer")  # criar histograma
    st.plotly_chart(fig, use_container_width=True)  # exibir um gráfico Plotly interativo

if build_dis: # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')

    fig1 = px.scatter(car_data, x="odometer")  # criar histograma
    st.plotly_chart(fig1, use_container_width=True)  # exibir um gráfico Plotly interativo
