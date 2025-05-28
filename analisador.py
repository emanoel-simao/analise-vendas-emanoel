import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Análise de Vendas de Emanoel')

uploaded_file = st.file_uploader('Escolha um arquivo do Excel ou CSV', type=["xlsx", "csv"])

if uploaded_file is not None:
   
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file, engine='openpyxl')

   
    df['Data'] = pd.to_datetime(df['Data'], errors='coerce')
    df['Receita'] = pd.to_numeric(df['Receita'], errors='coerce')
    df = df.dropna(subset=['Data', 'Receita'])

    st.write('### Dados do Excel')
    st.dataframe(df)

 
    st.write('### Receita por categoria')
    receita_categoria = df.groupby('Categoria')['Receita'].sum().reset_index()
    fig = px.bar(receita_categoria, x='Categoria', y='Receita', title='Receita por categoria')
    st.plotly_chart(fig)


    st.write('### Receita ao longo do tempo')
    receita_tempo = df.groupby('Data')['Receita'].sum().reset_index()
    receita_tempo = receita_tempo.sort_values('Data')
    fig2 = px.line(receita_tempo, x='Data', y='Receita', title='Receita ao longo do tempo')
    st.plotly_chart(fig2)

