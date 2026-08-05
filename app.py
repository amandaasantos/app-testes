import streamlit as st
import pandas as pd

st.title("APP Testes")
st.subheader("Subtítulo do app testes")
st.write("Este é um aplicativo de teste usando Streamlit para criar uma interface")

# Lê o CSV normalmente
df = pd.read_csv('populacao.csv')

st.markdown("### Dados exploratórios da População")
st.dataframe(df)

# Gera o gráfico de barras
st.bar_chart(df, x="municipio", y="populacao", use_container_width=True)