import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

import My_Pages.Relatorio_Paciente.Encaminhado_Por_Medico as Medico
import My_Pages.Relatorio_Paciente.Encaminhado_Por_Praca as Praca
import My_Pages.Relatorio_Paciente.Encaminhado_Por_Data as Data



def inicioPagina():
    logo_teste = Image.open('./Image/logo_oncoclinicas_horiozontal.jpg')
    st.image(logo_teste, use_column_width=True)
    st.markdown("<h1 style='text-align: center; color: blue;'></br></h1>", unsafe_allow_html=True)

def cabecalhoPagina():
    
    selected3 = option_menu(None, ["Encaminhados Por Médico", "Encaminhados Por Praça",  "Encaminhados Por Data"], 
        icons=['bi bi-hospital', 'bi bi-geo-alt', 'bi bi-calendar-check'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )
    #Titulo Inicial
    st.header('Relatório Pacientes Encaminhado(s)')
    return selected3

def analisePacienteEncaminhado():
    # Include Google Analytics tracking code
    with open("./google_analytics.html", "r") as f:
        html_code = f.read()
        components.html(html_code, height=0)
        st.title("My Streamlit App")
    
    resultado = cabecalhoPagina()
    
    if resultado == "Encaminhados Por Médico":
       Medico.analisePacienteEncaminhadoPorMedico()

    if resultado == "Encaminhados Por Praça":
        Praca.paginaPacienteEncaminhadoPorPraca()
    
    if resultado == "Encaminhados Por Data":
        Data.paginaPacienteEncaminhadoPorData()

def paginaPacienteEncaminhado():
    inicioPagina()
    analisePacienteEncaminhado()
