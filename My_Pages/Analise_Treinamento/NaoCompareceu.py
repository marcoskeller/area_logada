import streamlit as st
import pandas as pd





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
        nrows=238

    )
    return df

def totalMedicosNaCompareceram():
    df = gerar_df()

    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça','Treinamento', 'Quantidade Realizada']
    
    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 

    dadosUsuario = df

    #Filtro para trazer somente os médicos que estao aguardando agendamento
    dadosUsuario = df.loc[(
            df['Treinamento'] == "NÃO COMPARECEU")
        ]
    quantidadeTotalMedicosAguardandoTreinamento =  len(dadosUsuario)
    
    return quantidadeTotalMedicosAguardandoTreinamento

def nomeTodosMedicosNaoCompareceram(opcao):
    if opcao == '2 - SIM':
        df = gerar_df()

        #Seleciona somente as colunas uteis
        colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça','Treinamento', 'Contato Medico Apos treinamento']
    
        #Cria um dataFrame com as colunas uteis
        df = df[colunaUteis] 

        dadosUsuario = df
        
        dadosUsuario = df.loc[(
            df['Treinamento'] == "NÃO COMPARECEU")
        ]
        
        # Exibir o DataFrame filtrado
        st.dataframe(dadosUsuario, use_container_width=True, hide_index=True)
    else:
        print()

def quantidadeMedicosNaoCompareceramPorPraca(opcao):
    if opcao == "2 - SIM":
        df = gerar_df()

        #Seleciona somente as colunas uteis
        colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça','Treinamento', 'Quantidade Realizada']
        
        #Cria um dataFrame com as colunas uteis
        df = df[colunaUteis] 

        dadosUsuario = df

        #Filtro da Praça dos Medicos Selecionadaos
        dadosUsuario = df.loc[(
            df['Treinamento'] == "NÃO COMPARECEU")
        ]

        resultado = dadosUsuario.value_counts(dadosUsuario['Praça'])
        st.write(resultado)  
    else:
        print()

def exibirMedicosNaoCompareceramPorPraca(opcao):
    
    if opcao == "2 - SIM":

        df = gerar_df()

        #Seleciona somente as colunas uteis
        colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça','Treinamento']
    
        #Cria um dataFrame com as colunas uteis
        df = df[colunaUteis] 

        dadosUsuario = df

        #Filtro da Praça dos Medicos Selecionadaos
        dadosUsuario = df.loc[(
            df['Treinamento'] == "NÃO COMPARECEU")
        ]

        # função para selecionar a quantidade de linhas do dataframe
        def mostra_qntd_linhas(df_categoria):
    
            qntd_linhas = st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela', min_value = 0, max_value = len(df_categoria), step = 1)
            st.dataframe(df_categoria.head(qntd_linhas).style.format(subset = 'Treinamento'), use_container_width=True, hide_index=True)


        # filtros para a tabela
        checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')

        if checkbox_mostrar_tabela:

            st.sidebar.markdown('## Filtro para a tabela')

            categorias = list(dadosUsuario['Praça'].unique())
            categorias.append('Praça')

            categoria = st.sidebar.selectbox('Selecione a categoria para apresentar na tabela', options = categorias)

            if categoria != 'Praça':
                df_categoria = dadosUsuario.query('Praça == @categoria')            
                mostra_qntd_linhas(df_categoria)      
            else:
                mostra_qntd_linhas(dadosUsuario)
    else:
        print()

def filtroUteis():
    #Filtro Para Escola das Opcoes
    opcao = ['1 - NÃO', '2 - SIM']

    #Filtro Para Buscar o total de Médicos Aguardando Agendamento
    st.markdown('**Total de Médicos Que Não Compareceram:** ' + str(totalMedicosNaCompareceram()))

    #Exibi os Nomes dos Médicos que Aguardam Agendamento
    nomeTodosMedicosNaoCompareceram(st.selectbox("Deseja Exibir Todos o(s) Nome(s) do(s) Médico()s que Não Compareceram", options=opcao))

    #Exibi Quantidade Aguardam Agendamento Por Praça
    quantidadeMedicosNaoCompareceramPorPraca(st.selectbox("Deseja Exibir Quantidade de Médico(s) que Não Compareceram Por Praça", options=opcao))

    #Exibi Quantidade Aguardam Agendamento Por Praça
    exibirMedicosNaoCompareceramPorPraca(st.selectbox("Deseja Exibi o Nome do(s) Médico(s) que Não Compareceram por Praça", options=opcao))

def paginaNaoCompareceu():
    filtroUteis()