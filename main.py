import streamlit as st
from streamlit_option_menu import option_menu
import My_Pages.Pacientes_Encaminhados as Pacientes_Encaminhados
import My_Pages.PaginaInicial as PaginaInicial
import My_Pages.Relatorio as Relatorio

#Configuracao do Nome do Site
st.set_page_config(
    page_title="Área Logada",
    layout="wide"
)


#Menu Lateral
with st.sidebar:
    selected=option_menu(
        menu_title="Menu", 
        options=["Home", 'Pacientes Encaminhados', 'Relatórios'], 
        icons=['house', 'bi bi-calendar-week', 'bi bi-hospital', 'bi bi-clipboard-data'], 
        menu_icon = "cast", 
        default_index=0)
    


#Selecionando uma Pagina
if selected == "Home":
    PaginaInicial.paginaInicial()

if selected == "Pacientes Encaminhados":
    Pacientes_Encaminhados.paginaPacienteEncaminhado()

if selected == "Relatórios":
    Relatorio.paginaRelatorio()








