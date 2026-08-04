
import streamlit as st 
st.title ("APP Testes")
st.subheader ("Substitulo do app testes")
st.write ("Este é um aplicativo de teste usado Streamlit para criar uma interface")

import pandas as pd
df = pd.read_csv('populacao.csv')
st.markdown (""" #Dados exploratórios da População""")
st.dataframe (df)
st.bar_chart(df, x="municipio", y="populacao", use_container_width=True)
