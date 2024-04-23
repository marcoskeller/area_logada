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
        nrows=62

    )
    return df


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

            #Exibi o DataFrame que foi filtrado
            st.dataframe(df_filtered.astype(str), use_container_width=True, hide_index=True)


def quantidadePacienteEncaminhadoPorPraca(opcao):
    if opcao == "2 - Exibir":
        #Busca os Dados Gerados
        df = gerar_df()

        df_filtered = df

        resultado = df_filtered.value_counts(df_filtered['UF do Médico'])
        st.write(resultado)
    else:
        print()


def graficoPorPraca(opcao):
    if opcao == "2 - Exibir":
        #Busca os Dados Gerados
        df = gerar_df()

        #Seleciona somente as colunas uteis
        colunaUteis = ['Nome do Paciente', 'Data - Hora de abertura','Unidade que recebe paciente encaminhado', 'Nome do Médico', 'CRM','UF do Médico','Quantidade']
                
        #Cria um dataFrame com as colunas uteis
        df = df[colunaUteis] 

        df_filtered = df
                       
        #Calcular os Pacientes Encaminhados Por Medico
        paciente_total = df_filtered.groupby("UF do Médico")[["Quantidade"]].sum().reset_index()


        #Filtros Exibicao dos Nomes dos Pacientes
        checkbox_mostrar_graficoPizza = st.sidebar.checkbox('Exibir Gráfico Modelo Pizza')
        checkbox_mostrar_graficoBarra = st.sidebar.checkbox('Exibir Grafico Modela Barra')
                   
    
        if checkbox_mostrar_graficoPizza:
            #Grafico Pizza
            fig_kind = px.pie(paciente_total, values="Quantidade", names="UF do Médico",
            title="Total de pacientes Encaminhados Por Praça Até o Presente")
            st.plotly_chart(fig_kind, use_container_width=True)
            
        if  checkbox_mostrar_graficoBarra:
            # Criar o gráfico de barras para exibir o faturamento por cidade
            fig_paciente = px.bar(paciente_total, x="UF do Médico", y="Quantidade",
            title="Quantidade Pacientes Encaminhados Por Praça")
            # Exibir o gráfico
            st.plotly_chart(fig_paciente, use_container_width=True)
        else:
            print()

@st.cache_data()
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

        #Exibi o DataFrame que foi filtrado
        st.dataframe(df_filtered.astype(str), use_container_width=True, hide_index=True)


def filtroUteis():
    #Busca os Dados Gerados
    df = gerar_df()

    dadosUsuario = df

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
    filtroUteis()
 
 
def paginaPacienteEncaminhadoPorPraca():
    analisePacienteEncaminhado()
