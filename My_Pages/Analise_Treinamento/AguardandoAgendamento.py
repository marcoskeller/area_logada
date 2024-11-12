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
        nrows=241

    )
    return df

def medicosAguardandoAgendamento():
    df = gerar_df()

    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça','Treinamento']
    
    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 

    dadosUsuario = df

    #Filtro para trazer somente os médicos que estao aguardando agendamento
    dadosUsuario = df.loc[(
            df['Treinamento'] == "AGUARDANDO AGENDAMENTO")
        ]
    quantidadeTotalMedicosAguardandoTreinamento =  len(dadosUsuario)
    
    return quantidadeTotalMedicosAguardandoTreinamento

def nomeMedicosAguardamAgendamento(opcao):
    df = gerar_df()

    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça','Treinamento']
    
    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 

    dadosUsuario = df
    
    if opcao == "2 - SIM":

        dadosUsuario = df.loc[(
            df['Treinamento'] == "AGUARDANDO AGENDAMENTO")
        ]
        
        # Exibir o DataFrame filtrado
        st.dataframe(dadosUsuario, use_container_width=True, hide_index=True)
    else:
        print()
   
def graficoQuantidadeMedicosAguardamAgendamentoPorPraca(opcao):
    
    if opcao == "2 - SIM":
        df = gerar_df()

        #Seleciona somente as colunas uteis
        colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça','Treinamento']
        
        #Cria um dataFrame com as colunas uteis
        df = df[colunaUteis] 

        dadosUsuario = df

        #Filtro da Praça dos Medicos Selecionadaos
        dadosUsuario = df.loc[(
            df['Treinamento'] == "AGUARDANDO AGENDAMENTO")
        ]

        resultado = dadosUsuario.value_counts(dadosUsuario['Praça'])
        st.write(resultado)  
    else:
        print()
   
def selecaoPraca():
    #Chama funçao que obtem os dados
    df = gerar_df()

    #Seleciona somente as colunas uteis
    colunaUteis = ['Nome do Médico', 'Consultor/GO responsável','Praça','Treinamento']

    #Cria um dataFrame com as colunas uteis
    df = df[colunaUteis] 
    
    dadosUsuario = df

    ###Filtro Por Status do Treinamento
    dadosUsuario = df[df["Treinamento"] == "AGUARDANDO AGENDAMENTO" ]

    selecaoEstados = (dadosUsuario['Praça'].unique())

    
    return (selecaoEstados)

def filtroUteis():

    #Filtro Para Escola das Opcoes
    opcaoData = ['1 - NÃO', '2 - SIM']

    #Filtro Para Buscar o total de Médicos Aguardando Agendamento
    st.markdown('**Total de Médicos Aguardando Agendamento:** ' + str(medicosAguardandoAgendamento()))

    #Exibi os Nomes dos Médicos que Aguardam Agendamento
    nomeMedicosAguardamAgendamento(st.selectbox("Deseja Exibir o(s) Nome(s) do(s) Médico()s que Aguardam Agendamento", options=opcaoData))

    #Exibi Quantidade Aguardam Agendamento Por Praça
    graficoQuantidadeMedicosAguardamAgendamentoPorPraca(st.selectbox("Deseja Exibir Quantidade de Médico(s) que Aguardam Agendamento Por Praça", options=opcaoData))

def paginaAguardandoAgendamento():
    filtroUteis()
   