import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
import My_Pages.Pacientes_Encaminhados as Pacientes_Encaminhados
import My_Pages.PaginaInicial as PaginaInicial
import My_Pages.Relatorio as Relatorio

from bs4 import BeautifulSoup 
import pathlib 
import shutil 


def inject_ga():
    """Add this in your streamlit app.py
    see https://github.com/streamlit/streamlit/issues/969
    """
    # new tag method
    GA_ID = "google_analytics"
    # NOTE: you should add id="google_analytics" value in the GA script
    # https://developers.google.com/analytics/devguides/collection/analyticsjs
    GA_JS = """
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-QJ1VB0J4PK"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-QJ1VB0J4PK');
        </script>
        """
    # Insert the script in the head tag of the static template inside your virtual
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    soup = BeautifulSoup(index_path.read_text(), features="lxml")
    if not soup.find(id=GA_ID):  # if cannot find tag
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)  # recover from backup
        else:
            shutil.copy(index_path, bck_index)  # keep a backup
        html = str(soup)
        new_html = html.replace('<head>', '<head>\n' + GA_JS)
        index_path.write_text(new_html)


inject_ga()

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










