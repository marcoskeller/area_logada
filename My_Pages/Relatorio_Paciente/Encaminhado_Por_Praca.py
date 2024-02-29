import streamlit as st
import pandas as pd
import plotly.express as px



#Funcao para buscar os dados
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


def pacienteEncaminhadoPorPraca():
    
    #Busca os Dados Gerados
    df = gerar_df()
    
    dadosUsuario = df

    #funcao Retornar pacientes por nome do medico
    def selecaoPorPraca(praca):

        if not praca:
            print()
        else:
            #Busca os Dados Gerados
            df = gerar_df()

            ###Filtro Por Status do Treinamento
            df_filtered = df[df["UF do Médico"] == praca]

            #Seleciona somente as colunas uteis
            colunaUteis = ['Nome do Paciente', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'Nome do Médico', 'CRM']
            
            #Cria um dataFrame com as colunas uteis
            df_filtered = df_filtered[colunaUteis] 

            #df_filtered = df

            #Exibi o DataFrame que foi filtrado
            st.dataframe(df_filtered.astype(str), use_container_width=True)
    
    def graficoPorPraca(opcao):
        if opcao == "2 - Exibir":
            #Busca os Dados Gerados
            df = gerar_df()

            #Seleciona somente as colunas uteis
            colunaUteis = ['Nome do Paciente', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'Nome do Médico', 'CRM','UF do Médico','Quantidade']
                
            #Cria um dataFrame com as colunas uteis
            df = df[colunaUteis] 

            df_filtered = df
                       
            # Calcular os Pacientes Encaminhados Por Medico
            paciente_total = df_filtered.groupby("UF do Médico")[["Quantidade"]].sum().reset_index()

            # Criar o gráfico de barras para exibir o faturamento por cidade
            fig_paciente = px.bar(paciente_total, x="UF do Médico", y="Quantidade",
            title="Quantidade Pacientes Encaminhados Por Praça")

            # Exibir o gráfico
            st.plotly_chart(fig_paciente, use_container_width=True)    
        else:
            print()
           
    def quantidadePacienteEncaminhadoPorPraca(opcao):
        if opcao == "2 - Exibir":
            #Busca os Dados Gerados
            df = gerar_df()

            df_filtered = df

            resultado = df_filtered.value_counts(df_filtered['UF do Médico'])
            st.write(resultado)
        else:
            print()


    numeroTreinamentoRealizado = len(gerar_df())
    st.markdown('**Total de Paciente(s) Encaminhado(s):** ' + str(numeroTreinamentoRealizado))

    #Recebe o filtro que iremos utilizar
    selecaoPorPraca(st.selectbox("Pacientes Encaminhados Por Praça", dadosUsuario["UF do Médico"].unique(), None))

    #Filtro Para Exibiçao do Grafico
    #Criacao de Variaveis
    opcao = ['1 - Ocultar', '2 - Exibir']
    graficoPorPraca(st.selectbox("Gráfico Pacientes Encaminhados Por Praça", options=opcao))

    #Criacao de Variaveis
    opcao = ['1 - Ocultar', '2 - Exibir']
    quantidadePacienteEncaminhadoPorPraca(st.selectbox("Exibir Quatidade de Pacientes Encaminhados Por Praça", options=opcao))



def analisePacienteEncaminhado():
    pacienteEncaminhadoPorPraca()



def paginaPacienteEncaminhadoPorPraca():
    analisePacienteEncaminhado()
