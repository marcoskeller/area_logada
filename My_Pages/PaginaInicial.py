import streamlit as st
from PIL import Image



def paginaInicial():
    st.markdown("<h1 style='text-align: center; color: #6e9a6f;'>Treinamento Área Logada</h1>", unsafe_allow_html=True)
    #st.header('Treinamento Área Logada')

    logo_teste = Image.open('./Image/logo_oncoclinicas_basico_1.jpg')
    st.image(logo_teste, use_column_width=True)


