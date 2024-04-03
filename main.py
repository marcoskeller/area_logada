import streamlit as st
import streamlit.components.v1 as components
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
    google_analytics_js = """
    <!-- Global site tag (gtag.js) - Google Analytics -->
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-QJ1VB0J4PK"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-QJ1VB0J4PK');
        </script>
    """
    st.components.v1.html(google_analytics_js)
    PaginaInicial.paginaInicial()

if selected == "Pacientes Encaminhados":
    Pacientes_Encaminhados.paginaPacienteEncaminhado()

if selected == "Relatórios":
    Relatorio.paginaRelatorio()










