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
        nrows=129

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

    #Conversao de Data
    dadosUsuario["Data da realização do Treinamento"] = pd.to_datetime(df["Data da realização do Treinamento"], errors='coerce',utc=False)
    dadosUsuario['Data da realização do Treinamento'] = dadosUsuario['Data da realização do Treinamento'].dt.strftime('%b/%Y')
    dadosUsuario = dadosUsuario.sort_values("Data da realização do Treinamento")

    #Quantidade de Treinamento Por Consultor
    fig_kind = px.pie(dadosUsuario, values="Quantidade Realizada", names="Data da realização do Treinamento",
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

def contatoPosTreinamento(contato):
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


    if contato == "2 - Exibir":
        dadosUsuario = df.loc[(
            df['Contato Medico Apos treinamento'] == "SIM")
        ]
        
        # Exibir o DataFrame filtrado
        st.dataframe(dadosUsuario, use_container_width=True, hide_index=True)
        st.write( "Total Médicos Contactados: " , len(dadosUsuario))

        #Filtro da Praça dos Medicos Selecionadaos
        dadosUsuario = df.loc[(
            df['Contato Medico Apos treinamento'] == "SIM")
        ]


        #Criar o gráfico de barras para exibir o quantidade de medicos que receberam contato
        city_total = dadosUsuario.groupby("Praça")[["Quantidade Realizada"]].sum().reset_index()
        fig_city = px.bar(city_total, x="Praça", y="Quantidade Realizada",
        title="Quantidade Contato(s) Realizado(s) Pós Treinamento(s) Realizado Por Praça")
        st.plotly_chart(fig_city, use_container_width=True)    
    else:
        print()

def contatoNaoRealizadoPosTreinamento(contato):
    #Chama funçao que obtem os dados
    df = gerar_df()

    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça', 'Data da realização do Treinamento',
        'Treinamento', 'Contato Medico Apos treinamento', 'Onboarding Finalizado', 'Quantidade Realizada']
    
    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 

    dadosUsuario = df

    dadosUsuario["Data da realização do Treinamento"] = pd.to_datetime(df["Data da realização do Treinamento"], errors='coerce',utc=False)
    dadosUsuario['Data da realização do Treinamento'] = dadosUsuario['Data da realização do Treinamento'].dt.strftime('%m/%Y')


    if contato == "2 - Exibir":
        
        dadosUsuario = df.loc[(
            df['Treinamento'] == "REALIZADO") &
            (df['Contato Medico Apos treinamento'] == "NÃO")
        ]
        
        # Exibir o DataFrame filtrado
        st.dataframe(dadosUsuario, use_container_width=True, hide_index=True)
        st.write( "Total Médico(s) que não foram Contactados Pós Treinamento: " , len(dadosUsuario))

        dadosUsuario = df.loc[(
            df['Contato Medico Apos treinamento'] == "NÃO")
        ]

        #Criar o gráfico de barras para exibir o quantidade de medicos que receberam contato
        city_total = dadosUsuario.groupby("Praça")[["Quantidade Realizada"]].sum().reset_index()
        fig_city = px.bar(city_total, x="Praça", y="Quantidade Realizada",
        title="Quantidade de Médico(s)Que Não Receberam Contato Pós Treinamento")
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
            df['Treinamento'] != "REALIZADO")
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
   
    #Recebe o filtro que iremos utilizar
    contatoPosTreinamento(st.selectbox("Total de Médico(s) que foram contactados Pós Treinamento", options=opcaoData))

    #Recebe o filtro que iremos utilizar
    contatoNaoRealizadoPosTreinamento(st.selectbox("Total de Médico(s) que não foram contactados Pós Treinamento", options=opcaoData))  

def paginaRealizadoInicial():
    filtroUteis()


