import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Analise de vendas de Emanoel')

uploaded_file = st.file_uploader('Escolha um arquivo do excel', type=["xlsx", "csv"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, engine='openpyxl')

    st.write('### Dados do excel')
    st.dataframe(df)

    st.write('### Receita por categoria')
    receita_categoria = df.groupby('Categoria')['Receita'].sum().reset_index()
    fig = px.bar(receita_categoria, x='Categoria', y= 'Receita', title='Receita por categoria')
    st.plotly_chart(fig)

    st.write('### Receita ao longo do tempo')
    receita_tempo = df.groupby('Data')['Receita'].sum().reset_index()
    fig2 = px.line(receita_tempo, x='Data', y='Receita', title='Receita ao longo do tempo')

