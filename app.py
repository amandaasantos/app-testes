import streamlit as st
import pandas as pd

st.title("APP Testes")
st.subheader("Subtítulo do app testes")
st.write("Este é um aplicativo de teste usando Streamlit para criar uma interface")

# Tenta ler com vírgula ou ponto e vírgula
try:
    df = pd.read_csv('populacao.csv')
    if len(df.columns) == 1:
        df = pd.read_csv('populacao.csv', sep=';')
except Exception:
    df = pd.read_csv('populacao.csv', sep=';')

# Remove espaços nos nomes das colunas e deixa em minúsculo
df.columns = df.columns.str.strip().str.lower()

st.markdown("### Dados exploratórios da População")
st.dataframe(df)

# Gera o gráfico com as colunas ajustadas
st.bar_chart(df, x="municipio", y="populacao", use_container_width=True)