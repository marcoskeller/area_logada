import streamlit as st
import pandas as pd
import plotly.express as px


#Funcao para buscar os dados
@st.cache_data()
def gerar_df():
    
    #Configuracao para Acessar os Dados mais rapidos
    #@st.cache_data()
    df = pd.read_excel(
        io = "prj_imunomediados _controle_onboarding_21_02_2024.xlsx",
        engine="openpyxl",
        sheet_name="Dados_Onboarding",
        usecols="A:Y",
        nrows=241

    )
    return df

def treinamentoRealizadoPorPraca(estado):
    #Chama funçao que obtem os dados
    df = gerar_df()


    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça', 'Data da realização do Treinamento',
                'Treinamento', 'Objeção para Realizar Parte Administrativa','Onboarding Finalizado', 'Quantidade Realizada']

    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 

    dadosUsuario = df

    dadosUsuario["Data da realização do Treinamento"] = pd.to_datetime(df["Data da realização do Treinamento"], errors='coerce',utc=False)
    dadosUsuario['Data da realização do Treinamento'] = dadosUsuario['Data da realização do Treinamento'].dt.strftime('%m/%Y')

    ##Plotagem do Grafico
    ###Filtro Por Status do Treinamento
    df_filtered = df[df["Praça"] == estado ]

    dadosUsuario = df.loc[(
        df['Praça'] == estado) &
        (df['Treinamento'] == "Realizado")
    ]

    #Exibicao do Grafico
    if not estado:
        print() 
    else:
        ##Contribuição por Estado
        city_total = df_filtered.groupby("Praça")[["Quantidade Realizada"]].sum().reset_index()

        # Criar o gráfico de barras para exibir o faturamento por cidade
        fig_city = px.bar(city_total, x="Praça", y="Quantidade Realizada",
        title="Quantidade Treinamento(s) Realizado Por Praça")

        # Exibir o gráfico
        st.plotly_chart(fig_city, use_container_width=True)
    
def treinamentoRealizadoPorData(data):
    #Chama funçao que obtem os dados
    df = gerar_df()

    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça', 'Data da realização do Treinamento',
                'Treinamento', 'Objeção para Realizar Parte Administrativa','Onboarding Finalizado', 'Quantidade Realizada']

    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 

    dadosUsuario = df

    #Parte que foi modficada
    dadosUsuario = df.loc[
        (df['Treinamento'] == "REALIZADO")
    ]

    

    #Conversao de Data
    dadosUsuario["Data da realização do Treinamento"] = pd.to_datetime(df["Data da realização do Treinamento"], errors='coerce',utc=False)
    dadosUsuario['Data da realização do Treinamento'] = dadosUsuario['Data da realização do Treinamento'].dt.strftime('%b/%Y')
    dadosUsuario = dadosUsuario.sort_values("Data da realização do Treinamento")


    ##Contribuição por Estado
    quantidade_mes = dadosUsuario.groupby("Data da realização do Treinamento")[["Quantidade Realizada"]].sum().reset_index()

    #Quantidade de Treinamento Por Mes
    #dadosUsuario = dadosUsuario.groupby("Praça")[["Quantidade Realizada"]].sum().reset_index()
    fig_kind = px.bar(quantidade_mes, x="Data da realização do Treinamento", y="Quantidade Realizada",
    title="Treinamento(s) Realizado(s) Por Mês Até o Presente")
    
    if data == "2 - Exibir":
        st.plotly_chart(fig_kind, use_container_width=True)    
    else:
        print()

def totalTreinamentoRealizados(status):
    #Chama funçao que obtem os dados
    df = gerar_df()

    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça', 'Data da realização do Treinamento',
                'Treinamento', 'Objeção para Realizar Parte Administrativa','Onboarding Finalizado', 'Quantidade Realizada']

    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 

    ###Filtro Por Status do Treinamento
    df_filtered = df[df["Treinamento"] == "REALIZADO" ]

    dadosUsuario = df.loc[(
        (df['Treinamento'] == "REALIZADO"))]

    ##Contribuição por Estado
    city_total = df_filtered.groupby("Praça")[["Quantidade Realizada"]].sum().reset_index()

    # Criar o gráfico de barras para exibir o faturamento por cidade
    fig_city = px.bar(city_total, x="Praça", y="Quantidade Realizada",
    title="Quantidade Treinamento(s) Realizado Por Praça")

    if status == "2 - Exibir":
        # Exibir o gráfico
        st.plotly_chart(fig_city, use_container_width=True)   
    else:
        print()

def numeroTreinamentoRealizado():
    #Chama funçao que obtem os dados
    df = gerar_df()

    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça', 'Data da realização do Treinamento',
        'Treinamento', 'Objeção para Realizar Parte Administrativa', 'Contato Medico Apos treinamento', 'Onboarding Finalizado', 'Quantidade Realizada']
    
    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 

    dadosUsuario = df

    dadosUsuario["Data da realização do Treinamento"] = pd.to_datetime(df["Data da realização do Treinamento"], errors='coerce',utc=False)
    dadosUsuario['Data da realização do Treinamento'] = dadosUsuario['Data da realização do Treinamento'].dt.strftime('%m/%Y')

    dadosUsuario = df.loc[(
            df['Treinamento'] == "REALIZADO")
        ]
    quantidadeTotalTreinamentoRealizado =  len(dadosUsuario)
    
    return quantidadeTotalTreinamentoRealizado

def numeroNaoTreinamentoRealizado():
    #Chama funçao que obtem os dados
    df = gerar_df()

    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça', 'Data da realização do Treinamento',
        'Treinamento', 'Objeção para Realizar Parte Administrativa', 'Contato Medico Apos treinamento', 'Onboarding Finalizado', 'Quantidade Realizada']
    
    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 

    dadosUsuario = df

    dadosUsuario["Data da realização do Treinamento"] = pd.to_datetime(df["Data da realização do Treinamento"], errors='coerce',utc=False)
    dadosUsuario['Data da realização do Treinamento'] = dadosUsuario['Data da realização do Treinamento'].dt.strftime('%m/%Y')

    dadosUsuario = df.loc[(
            df['Treinamento'] == "AGUARDANDO AGENDAMENTO")
        ]
    quantidadeTotalTreinamentoNaoRealizado =  len(dadosUsuario)
    
    return quantidadeTotalTreinamentoNaoRealizado

def filtroUteis():

    #Criacao de Variaveis
    opcaoData = ['1 - Ocultar', '2 - Exibir']

    st.markdown('**Total de Treinamentos Realizados:** ' + str(numeroTreinamentoRealizado()))
    st.markdown('**Total de Treinamentos que Falta Realizar**: ' + str(numeroNaoTreinamentoRealizado()))

    #Chama funçao que obtem os dados
    df = gerar_df()


    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça', 'Data da realização do Treinamento',
                'Treinamento', 'Objeção para Realizar Parte Administrativa','Onboarding Finalizado', 'Quantidade Realizada']

    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 

    dadosUsuario = df

    dadosUsuario["Data da realização do Treinamento"] = pd.to_datetime(df["Data da realização do Treinamento"], errors='coerce',utc=False)
    dadosUsuario['Data da realização do Treinamento'] = dadosUsuario['Data da realização do Treinamento'].dt.strftime('%m/%Y')
    dadosUsuario = dadosUsuario.sort_values("Data da realização do Treinamento")

    #st.sidebar.title('Menu')
    st.subheader('Seleção de Filtros')

    
    #Recebe o filtro que iremos utilizar
    totalTreinamentoRealizados(st.selectbox("Total de Treinamento(s) Realizado(s) Por Praça", options=opcaoData))

    #Recebe o filtro que iremos utilizar
    treinamentoRealizadoPorPraca(st.selectbox("Treinamento(s) Realizado(s) Por Praça", dadosUsuario["Praça"].unique(), None))

    #Recebe o filtro que iremos utilizar
    treinamentoRealizadoPorData(st.selectbox("Total de Treinamento(s) Realizado(s) Por Mês Até o Momento",opcaoData))
   
def paginaRealizadoInicial():
    filtroUteis()


