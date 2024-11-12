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

def treinamentoRealizadoPorPraca(opcao):
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



    #Filtro dos Status do Treinamento
    dadosUsuario = df.loc[
        (df['Treinamento'] == "REALIZADO")
    ]

    #Exibicao do Resultado
    if opcao == "2 - Exibir":
        resultado = dadosUsuario.value_counts(dadosUsuario['Praça'])
        st.write(resultado)
    else:
        print()
    
def treinamentoRealizadoPorData(data):
    #Chama funçao que obtem os dados
    df = gerar_df()

    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça', 'Data da realização do Treinamento',
                'Treinamento', 'Objeção para Realizar Parte Administrativa','Onboarding Finalizado', 'Quantidade Realizada']

    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 

    dadosUsuario = df
    

    #Filtro da Praça dos Medicos Selecionadaos
    dadosUsuario = df.loc[
        (df['Treinamento'] == "REALIZADO")
    ]

    dadosOrganizado = dadosUsuario
    filtroMesAnoTeste = dadosUsuario

    #Conversao de Data
    dadosUsuario["Data da realização do Treinamento"] = pd.to_datetime(df["Data da realização do Treinamento"], errors='coerce',utc=False)
    dadosUsuario['Data da realização do Treinamento'] = dadosUsuario['Data da realização do Treinamento'].dt.strftime('%b/%Y')
    dadosUsuario = dadosUsuario.sort_values("Data da realização do Treinamento")


    dadosUsuarioAno = dadosUsuario

    if data == "2 - Exibir":

        #Filtro Para Mostrar o Ano
        dadosUsuarioAno["Data da realização do Treinamento"] = pd.to_datetime(df["Data da realização do Treinamento"], errors='coerce',utc=False, dayfirst=True)
        dadosUsuarioAno['Data da realização do Treinamento'] = dadosUsuarioAno['Data da realização do Treinamento'].dt.strftime('%Y')
        dadosUsuarioAno = dadosUsuarioAno.sort_values("Data da realização do Treinamento")
        selecioneAno = list(dadosUsuarioAno['Data da realização do Treinamento'].unique())
        
        st.sidebar.markdown('## Escolha o Ano')
        ano = st.sidebar.selectbox('', options = selecioneAno)

        ##Filtro Por Ano Funcionando
        #dadosUsuarioAno = dadosUsuarioAno.loc[(
        #    dadosUsuarioAno['Data da realização do Treinamento'] == str(ano))
        #]
        
        if ano != '':
            filtroMesAno = dadosUsuario
             
            #Filtrando a Data
            filtroMesAno["Data da realização do Treinamento"] = pd.to_datetime(dadosOrganizado["Data da realização do Treinamento"], errors='coerce', dayfirst=True)
            filtroMesAno["Data da realização do Treinamento"] = filtroMesAno["Data da realização do Treinamento"].dt.strftime('%m/%Y')
            filtroMesAno = filtroMesAno.sort_values("Data da realização do Treinamento")


            # Criando nova coluna
            filtroMesAno['Ano'] = '00/00/0000'

            #Adcionando o Ano na nova coluna
            filtroMesAno["Ano"] = pd.to_datetime(dadosOrganizado["Data da realização do Treinamento"], errors='coerce',dayfirst=True, utc=False)
            filtroMesAno["Ano"] = pd.to_datetime(dadosOrganizado["Data da realização do Treinamento"], errors='coerce', dayfirst=True)
            filtroMesAno["Ano"] = filtroMesAno["Ano"].dt.strftime('%Y')
            filtroMesAno = filtroMesAno.sort_values("Ano")

            #Filtro Para Trazer somente o Ano Desejado
            filtroMesAno = filtroMesAno.loc[(
                filtroMesAno['Ano'] == str(ano))
            ]


            ###Grafico Exibindo Apenas o Ano Informado
            city_total = filtroMesAno.groupby("Data da realização do Treinamento")[["Quantidade Realizada"]].sum().reset_index()

            #Grafico Barra
            fig_city = px.bar(city_total, x="Data da realização do Treinamento", y="Quantidade Realizada",
            title="Quantidade Treinamento(s) Realizado Mês")
            
            #Plotagem do Grafico
            st.plotly_chart(fig_city, use_container_width=True)



            # ###Grafico Exibindo Todos os Anos juntos
            # ##Contribuição por Estado
            # city_total = filtroMesAno.groupby("Data da realização do Treinamento")[["Quantidade Realizada"]].sum().reset_index()

            # #Grafico Barra
            # fig_city = px.bar(city_total, x="Data da realização do Treinamento", y="Quantidade Realizada",
            # title="Quantidade Treinamento(s) Realizado Mês")
            
            # #Plotagem do Grafico
            # st.plotly_chart(fig_city, use_container_width=True)

        else:
            st.write("É necessário selecionar o ano!")
     


        #st.plotly_chart(fig_kind, use_container_width=True) 
    else:
        print("Entrou no Else")

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
    totalTreinamentoRealizados(st.selectbox("Gráfico do Total de Treinamento(s) Realizado(s) Por Praça", options=opcaoData))

    #Recebe o filtro que iremos utilizar
    treinamentoRealizadoPorPraca(st.selectbox("Total de Treinamento(s) Realizado(s) Por Praça", options=opcaoData))

    #Recebe o filtro que iremos utilizar
    treinamentoRealizadoPorData(st.selectbox("Gráfico do Total de Treinamento(s) Realizado(s) Por Mês Até o Momento",opcaoData))
   
def paginaRealizadoInicial():
    filtroUteis()


