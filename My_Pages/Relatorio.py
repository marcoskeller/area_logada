import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import My_Pages.Analise_Treinamento.Realizado as Treinamento_Realizado
import My_Pages.Analise_Treinamento.AguardandoAgendamento as Aguardando_Agendamento
import My_Pages.Analise_Treinamento.NaoCompareceu as Nao_Compareceu
import My_Pages.Analise_Treinamento.Agendado as Agendado

#Funcao Para Exibir Cabecalho
def inicioPagina():
    logo_teste = Image.open('./Image/logo_oncoclinicas_horiozontal.jpg')
    st.image(logo_teste, use_column_width=True)
    st.markdown("<h1 style='text-align: center; color: blue;'></br></h1>", unsafe_allow_html=True)
    

def cabecalhoPagina():
    
    #3. CSS style definitions
    selected3 = option_menu(None, ["Realizado", "Aguardando",  "Não Compareceu", 'Agendado'], 
        icons=['bi bi-clipboard2-check-fill', 'bi bi-clock', "bi bi-exclamation-diamond", 'bi bi-calendar-check-fill'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )
    #Titulo Inicial
    st.header('Relatório Treinamento Área Logada')
    return selected3

#Filtro Pra Buscar os Agendamento Realizados
def agendamentosRealizados():
    Treinamento_Realizado.paginaRealizadoInicial()
     

def analiseTreinamentoRealizado():
    
    resultado = cabecalhoPagina()
    
    if resultado == "Realizado":
       agendamentosRealizados() 

    if resultado == "Aguardando":
        Aguardando_Agendamento.paginaAguardandoAgendamento()
    
    if resultado == "Não Compareceu":
        Nao_Compareceu.paginaNaoCompareceu()
    
    if resultado == "Agendado":
        Agendado.paginaAgendado()

def paginaRelatorio():
    inicioPagina()
    analiseTreinamentoRealizado()
        
