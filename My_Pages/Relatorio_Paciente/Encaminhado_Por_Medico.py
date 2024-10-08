import streamlit as st
import pandas as pd
import plotly.express as px



#Funcao para buscar os dados
@st.cache_data()
def gerar_df():
    
    #Configuracao para Acessar os Dados mais rapidos
    #@st.cache_data()
    df = pd.read_excel(
        io = "pacientes_imuno_mediados_encaminhados_27_02-2024.xlsx",
        engine="openpyxl",
        sheet_name="Encaminhamento Imuno",
        usecols="A:H",
        nrows=262

    )
    return df


##Para mostrar o total de pacientes encaminhados excluindos os pacientes testes
def total_Pacientes_encaminhados_excluindo_Teste():
    
    total_pacientes = gerar_df()
    
    total_Pacientes_Encaminhados = total_pacientes[["Quantidade"]].sum()
    
    return total_Pacientes_Encaminhados[0]


def pacienteEncaminhadoPorMedico():
    
    #Busca os Dados Gerados
    df = gerar_df()
    
    dadosUsuario = df

    #funcao Retornar pacientes por nome do medico
    def selecaoPorNomeMedico(nomeMedico):

        if not nomeMedico:
            print()
        else:
            #Busca os Dados Gerados
            df = gerar_df()

            #Seleciona somente as colunas uteis
            colunaUteis = ['Nome do Paciente', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'Nome do Médico','CRM','UF do Médico']
            
            #Cria um dataFrame com as colunas uteis
            df = df[colunaUteis] 

            df_filtered = df
            
            ###Filtro Por Status do Treinamento
            df_filtered = df[df["Nome do Médico"] == nomeMedico ]

            #Exibi o DataFrame que foi filtrado
            st.dataframe(df_filtered.astype(str), use_container_width=True, hide_index=True)
    
    def graficoPorNomeMedico(opcao):
        if opcao == "2 - Exibir":
            #Busca os Dados Gerados
            df = gerar_df()

            #Seleciona somente as colunas uteis
            colunaUteis = ['Nome do Médico', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'CRM','UF do Médico','Quantidade']
                
            #Cria um dataFrame com as colunas uteis
            df = df[colunaUteis] 

            df_filtered = df
                       
            # Calcular os Pacientes Encaminhados Por Medico
            paciente_total = df_filtered.groupby("Nome do Médico")[["Quantidade"]].sum().reset_index()

            # Criar o gráfico de barras para exibir o faturamento por cidade
            fig_paciente = px.bar(paciente_total, x="Nome do Médico", y="Quantidade",
            title="Quantidade Pacientes Encaminhados Por Médico")

            # Exibir o gráfico
            st.plotly_chart(fig_paciente, use_container_width=True)    
        else:
            print()
           
    def quantidadePacienteEncaminhadoPorMedico(opcao):
        if opcao == "2 - Exibir":
            #Busca os Dados Gerados
            df = gerar_df()

            #Seleciona somente as colunas uteis
            colunaUteis = ['Nome do Médico', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'CRM','UF do Médico']
                    
            #Cria um dataFrame com as colunas uteis
            df = df[colunaUteis] 

            df_filtered = df

            resultado = df_filtered.value_counts(df_filtered['Nome do Médico'])
            st.write(resultado)
        else:
            print()


    st.markdown('**Total de Paciente(s) Encaminhado(s):** ' + str(total_Pacientes_encaminhados_excluindo_Teste()))

    #Recebe o filtro que iremos utilizar
    selecaoPorNomeMedico(st.selectbox("Pacientes Encaminhados Por Médico", dadosUsuario["Nome do Médico"].unique(), None))

    #Filtro Para Exibiçao do Grafico
    #Criacao de Variaveis
    opcao = ['1 - Ocultar', '2 - Exibir']
    graficoPorNomeMedico(st.selectbox("Gráfico Pacientes Encaminhados Por Médico", options=opcao))

    #Criacao de Variaveis
    opcao = ['1 - Ocultar', '2 - Exibir']
    quantidadePacienteEncaminhadoPorMedico(st.selectbox("Exibir Quatidade de Pacientes Encaminhados Por Médico", options=opcao))


def analisePacienteEncaminhadoPorMedico():
    pacienteEncaminhadoPorMedico()


def paginaPacienteEncaminhado():
    analisePacienteEncaminhadoPorMedico()
