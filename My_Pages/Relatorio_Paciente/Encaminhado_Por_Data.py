import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data()
def gerar_df():  
    #Configuracao para Acessar os Dados mais rapidos
    #@st.cache_data()
    df = pd.read_excel(
        io = "pacientes_imuno_mediados_encaminhados_27_02-2024.xlsx",
        engine="openpyxl",
        sheet_name="Encaminhamento Imuno",
        usecols="A:H",
        nrows=43

    )
    return df

def selecaoPorMes(opcao):

    if opcao == '2 - Exibir':
        #Busca os Dados Gerados
        df = gerar_df()

        filtroMesAno = df

        #Seleciona somente as colunas uteis
        colunaUteis = ['Nome do Paciente', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'Nome do Médico', 'CRM','UF do Médico']
                
        #Cria um dataFrame com as colunas uteis
        df = df[colunaUteis] 

        filtroMesAno = df
 
        #Filtrando a Data
        filtroMesAno["Data - Hora de abertura"] = pd.to_datetime(df["Data - Hora de abertura"], errors='coerce', dayfirst=True)
        filtroMesAno['Data - Hora de abertura'] = filtroMesAno['Data - Hora de abertura'].dt.strftime('%m/%Y')
        filtroMesAno = filtroMesAno.sort_values("Data - Hora de abertura")


        selecioneMes = list(filtroMesAno['Data - Hora de abertura'].unique())
                
        
        st.sidebar.markdown('## Escolha o Mês')
        mes = st.sidebar.selectbox('', options = selecioneMes)

        #Filtro Para Trazer somente o mes desejado
        filtroMesAno = filtroMesAno.loc[(
            filtroMesAno['Data - Hora de abertura'] == str(mes))
        ]

        # Exibir o DataFrame filtrado Por Ano
        st.dataframe(filtroMesAno.astype(str), use_container_width=True, hide_index=True)
    else:
        print()

def graficoSelecaoPorMes(opcao):
    if opcao == '2 - Exibir':
        #Busca os Dados Gerados
        df = gerar_df()

        #Seleciona somente as colunas uteis
        colunaUteis = ['Nome do Paciente', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'Nome do Médico', 'CRM','UF do Médico','Quantidade']
         
        #Cria um dataFrame com as colunas uteis
        df = df[colunaUteis] 

        dadosUsuario = df

        #Filtrando Por Ano
        dadosUsuario["Data - Hora de abertura"] = pd.to_datetime(df["Data - Hora de abertura"], errors='coerce', dayfirst=True)
        dadosUsuario['Data - Hora de abertura'] = dadosUsuario['Data - Hora de abertura'].dt.strftime('%Y/%m')

        # Calcular os Pacientes Encaminhados Por Ano
        city_total = dadosUsuario.groupby("Data - Hora de abertura")[["Quantidade"]].sum().reset_index()

 
        ##Exibicao dos Graficos
        #Filtros Exibicao dos Nomes dos Pacientes
        checkbox_mostrar_graficoPizza = st.sidebar.checkbox('Exibir Gráfico Modelo Pizza')
        checkbox_mostrar_graficoBarra = st.sidebar.checkbox('Exibir Grafico Modela Barra')

        if checkbox_mostrar_graficoPizza:
            #Grafico Pizza
            fig_kind = px.pie(city_total, values="Quantidade", names="Data - Hora de abertura",
            title="Total de pacientes Encaminhados Por Mês Até o Presente")
            st.plotly_chart(fig_kind, use_container_width=True)
        
        if  checkbox_mostrar_graficoBarra:
            #Grafico Barra
            fig_city = px.bar(city_total, x="Data - Hora de abertura", y="Quantidade",
            title="Total de pacientes Encaminhados Por Mês Até o Presente")
            st.plotly_chart(fig_city, use_container_width=True)

        #Filtros Exibicao dos Nomes dos Pacientes
        checkbox_mostrar_tabela = st.sidebar.checkbox('Exibir Nome dos Pacientes Encaminhados')


        if checkbox_mostrar_tabela:
            #Seleciona somente as colunas uteis
            colunaUteis = ['Nome do Paciente', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'Nome do Médico', 'CRM','UF do Médico']

            #Cria um dataFrame com as colunas uteis
            df = df[colunaUteis] 

            dadosUsuario = df

            #Exibicao do Dataframe filtrado
            st.dataframe(dadosUsuario.astype(str), use_container_width=True, hide_index=True) 
    else:
        print()

def selecaoPorAno(opcao):
    
    if opcao == '2 - Exibir':
        #Busca os Dados Gerados
        df = gerar_df()

        #Seleciona somente as colunas uteis
        colunaUteis = ['Nome do Paciente', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'Nome do Médico', 'CRM','UF do Médico']
                
        #Cria um dataFrame com as colunas uteis
        df = df[colunaUteis] 

        dadosUsuarioAno = df

        #Filtrando Por Ano
        #df_filtered["Data - Hora de abertura"] = pd.to_datetime(df["Data - Hora de abertura"], errors='coerce',utc=False)
        dadosUsuarioAno["Data - Hora de abertura"] = pd.to_datetime(df["Data - Hora de abertura"], errors='coerce', dayfirst=True)
        dadosUsuarioAno['Data - Hora de abertura'] = dadosUsuarioAno['Data - Hora de abertura'].dt.strftime('%Y')
        dadosUsuarioAno = dadosUsuarioAno.sort_values("Data - Hora de abertura")


        selecioneAno = list(dadosUsuarioAno['Data - Hora de abertura'].unique())
        
        st.sidebar.markdown('## Escolha o Ano')
        ano = st.sidebar.selectbox('', options = selecioneAno)

        ##Filtro Por Ano Funcionando
        dadosUsuarioAno = dadosUsuarioAno.loc[(
            dadosUsuarioAno['Data - Hora de abertura'] == str(ano))
        ]

        #Exibicao do Dataframe filtrado
        st.dataframe(dadosUsuarioAno.astype(str), use_container_width=True, hide_index=True)
    else:
        print()

def graficoSelecaoPorAno(opcao):
    
    if opcao == '2 - Exibir':
        #Busca os Dados Gerados
        df = gerar_df()

        dadosUsuario = df

        #Seleciona somente as colunas uteis
        colunaUteis = ['Nome do Paciente', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'Nome do Médico', 'CRM','UF do Médico','Quantidade']
                
        #Cria um dataFrame com as colunas uteis
        df = df[colunaUteis] 

        #Filtrando Por Ano
        dadosUsuario["Data - Hora de abertura"] = pd.to_datetime(df["Data - Hora de abertura"], errors='coerce', dayfirst=True)
        dadosUsuario['Data - Hora de abertura'] = dadosUsuario['Data - Hora de abertura'].dt.strftime('%Y')
        dadosUsuario = dadosUsuario.sort_values("Data - Hora de abertura")

        
        # Calcular os Pacientes Encaminhados Por Ano
        city_total = dadosUsuario.groupby("Data - Hora de abertura")[["Quantidade"]].sum().reset_index()

        # Criar o gráfico de barras para exibir o faturamento por cidade
        fig_city = px.bar(city_total, x="Data - Hora de abertura", y="Quantidade",
        title="Quantidade Pacientes Encaminhados Por Ano")
        st.plotly_chart(fig_city, use_container_width=True)

        #Filtros Exibicao dos Nomes dos Pacientes
        checkbox_mostrar_tabela = st.sidebar.checkbox('Exibir Nome dos Pacientes Encaminhados')

        if checkbox_mostrar_tabela:
            #Seleciona somente as colunas uteis
            colunaUteis = ['Nome do Paciente', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'Nome do Médico', 'CRM','UF do Médico']

            #Cria um dataFrame com as colunas uteis
            df = df[colunaUteis] 

            dadosUsuario = df

            #Exibicao do Dataframe filtrado
            st.dataframe(dadosUsuario.astype(str), use_container_width=True, hide_index=True) 
    else:
        print()

def filtroUteis():
    #Criacao de Variaveis
    opcao = ['1 - Ocultar', '2 - Exibir']

    numeroTreinamentoRealizado = len(gerar_df())
    st.markdown('**Total de Paciente(s) Encaminhado(s):** ' + str(numeroTreinamentoRealizado))
    
    #Recebe o filtro que iremos utilizar
    selecaoPorMes(st.selectbox("Pacientes Encaminhados Por Mês", options=opcao))

    #filtro por Mes
    graficoSelecaoPorMes(st.selectbox("Grafico de Pacientes Encaminhados Por Mês", options=opcao))
   
    #filtro por Ano
    selecaoPorAno(st.selectbox("Pacientes Encaminhados Por Ano", options=opcao))

    #filtro por Ano
    graficoSelecaoPorAno(st.selectbox("Grafico de Pacientes Encaminhados Por Ano", options=opcao))

def paginaPacienteEncaminhadoPorData():
    filtroUteis()