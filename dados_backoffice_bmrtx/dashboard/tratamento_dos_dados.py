import dash
from dash import dcc, html
from dash.dependencies import Input,Output
import pandas as pd
import plotly.graph_objects as go
import gunicorn
from pprint import pprint
import streamlit as st
import numpy as np
from datetime import datetime,timedelta

st.set_page_config(layout = 'wide')

lista_pag =[0,1,2,3,4,5]
@st.cache_data


def le_excel(x,y):
    df_dic = pd.read_excel(x,y)
    return df_dic

btg = le_excel('Controle de Contratos - Atualizado 09.2023.xlsx',1)
guide = le_excel('Controle de Contratos - Atualizado 09.2023.xlsx',2)
genial = le_excel('Controle de Contratos - Atualizado 09.2023.xlsx',3)
agora = le_excel('Controle de Contratos - Atualizado 09.2023.xlsx',4)
orama = le_excel('Controle de Contratos - Atualizado 09.2023.xlsx',5)
novas = le_excel('Controle de Contratos - Atualizado 09.2023.xlsx',6)

###########



###########
# renomeando colunas periodo de 2023
# ##########

lista_core = [btg,guide,genial,agora,orama]
lista_core2 = [guide,genial]

for corretora in lista_core:
    nome_ultima_col = corretora.columns[-1]

    novo_nome = 'Outubro/2023'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core:
    nome_ultima_col = corretora.columns[-2]

    novo_nome = 'Setembro/2023'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)
    lista_core = [btg,guide,genial,agora,orama,novas]

for corretora in lista_core:
    nome_ultima_col = corretora.columns[-3]

    novo_nome = 'Agosto/2023'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core:
    nome_ultima_col = corretora.columns[-4]

    novo_nome = 'julho/2023'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core:
    nome_ultima_col = corretora.columns[-5]

    novo_nome = 'junho/2023'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)



for corretora in lista_core:
    nome_ultima_col = corretora.columns[-6]

    novo_nome = 'Maio/2023'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core:
    nome_ultima_col = corretora.columns[-7]

    novo_nome = 'Abril/2023'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)



for corretora in lista_core:
    nome_ultima_col = corretora.columns[-8]

    novo_nome = 'Março/2023'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-9]

    novo_nome = 'fereiro/2023'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-10]

    novo_nome = 'Janeiro/2023'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

    
###########
# renomeando colunas periodo de 2022
# ##########

for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-11]

    novo_nome = 'Dezembro/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-12]

    novo_nome = 'Novembro/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-13]

    novo_nome = 'Outubro/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-14]

    novo_nome = 'Setembro/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-15]

    novo_nome = 'Agosto/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-16]

    novo_nome = 'julho/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-17]

    novo_nome = 'junho/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)



for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-18]

    novo_nome = 'Maio/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-19]

    novo_nome = 'Abril/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-20]

    novo_nome = 'Março/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)



for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-21]

    novo_nome = 'fereiro/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-22]

    novo_nome = 'Janeiro/2022'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


###########
# renomeando colunas periodo de 2021
# ##########

for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-23]

    novo_nome = 'Dezembro/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-22]

    novo_nome = 'Novembro/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-24]

    novo_nome = 'Outubro/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-25]

    novo_nome = 'Setembro/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-26]

    novo_nome = 'Agosto/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-27]

    novo_nome = 'julho/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-28]

    novo_nome = 'junho/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)



for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-29]

    novo_nome = 'Maio/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-30]

    novo_nome = 'Abril/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-31]

    novo_nome = 'Março/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-32]

    novo_nome = 'fereiro/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-33]

    novo_nome = 'Janeiro/2021'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

###########
# renomeando colunas periodo de 2021
# ##########


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-34]

    novo_nome = 'Dezembro/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-35]

    novo_nome = 'Novembro/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-36]

    novo_nome = 'Outubro/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-37]

    novo_nome = 'Setembro/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-38]

    novo_nome = 'Agosto/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-39]

    novo_nome = 'julho/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-40]

    novo_nome = 'junho/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-41]

    novo_nome = 'Maio/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-42]

    novo_nome = 'Abril/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-43]

    novo_nome = 'Março/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-44]

    novo_nome = 'fereiro/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core2:
    nome_ultima_col = corretora.columns[-45]

    novo_nome = 'Janeiro/2020'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)


###########                        ###########
# Padrozinar as colunas de todos os df para conseguir concatenar o arquivo em seguida
# ##########                        ###########





###########        
# Tratando dados BTG
# ##########   

colunas_remover_btg = ['Mesa de Operação.1','Mesa de Operação.2',     
   'Gestão/ Head comercial',
   
  'Unnamed: 19',
   'Unnamed: 20',
  'Unnamed: 21',
   'Unnamed: 22',
  'Financeiro',
   'Unnamed: 24',
   'Unnamed: 25',
  'Unnamed: 26',
   'Unnamed: 27','Backoffice '
  ]
for colunas in colunas_remover_btg:
    btg.drop(columns=[colunas],inplace=True)
 
    ########### 
# Tratando dados GUIDE
# ##########   

colunas_remover_guide = [
'Unnamed: 15', 'Unnamed: 16',
'Unnamed: 17', 'Mesa de Operação ', 'Gestão/ Head comercial',
'Backoffice .2', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23',
'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27',
'Unnamed: 28', 'Unnamed: 29']

for col in colunas_remover_guide:
    guide.drop(columns=[col],inplace = True)

###########  
# Tratando dados GENIAL
# ##########  
colunas_remover_genial = [
    'Mesa de Operação ',
       'Gestão/ Head comercial', 'Backoffice ', 'Unnamed: 18', 'Unnamed: 19',
       'Unnamed: 20', 'Unnamed: 21', 'Financeiro', 'Unnamed: 23',
       'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26']

for col in colunas_remover_genial:
    genial.drop(columns=[col],inplace =True)



########### 
# Tratando dados Agora
# ##########      
colunas_remover_agora = [
    'Mesa de Operação ',
       'Gestão/ Head comercial', 'Backoffice ', 'Unnamed: 18', 'Unnamed: 19',
       'Unnamed: 20', 'Unnamed: 21']
for col in colunas_remover_agora:
    agora.drop(columns=[col],inplace=True)

###########     
# Tratando dados Agora
# ##########    
colunas_remover_orama = [ 'Mesa de Operação ', 'Backoffice ',
       'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20']
for col in colunas_remover_orama:
    orama.drop(columns=[col],inplace=True)



###########           ###########
# Tratando corrigindo nome das colunas 
# ##########           ###########    

for corretora in lista_core:
    nome_ultima_col = corretora.columns[0]

    novo_nome = 'Corretora'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[1]

    novo_nome = 'Nome_cliente'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[2]

    novo_nome = 'Conta'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[3]

    novo_nome = 'Escritorio'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[4]

    novo_nome = 'UF'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[5]

    novo_nome = 'Assessor'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[7]

    novo_nome = 'Status'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[8]

    novo_nome = 'Exeção'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[9]

    novo_nome = 'Inicio da gestão'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[10]

    novo_nome = 'Data do distrato'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[11]

    novo_nome = 'Carteira'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[12]

    novo_nome = 'Taxa de gestão'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[13]

    novo_nome = 'Benchmark'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    nome_ultima_col = corretora.columns[14]

    novo_nome = 'Taxa de performance'
    corretora.rename(columns={nome_ultima_col:novo_nome},inplace = True)

for corretora in lista_core:
    corretora = corretora.iloc[1:-5]



arquivo_final = pd.concat([btg,guide,genial,agora,orama]).reset_index()

arquivo_final.drop(columns=['index'],inplace=True)
arquivo_final.drop(988,inplace=True)
linhas_para_retirar = [588,593,983,984,985,986,987,1019,1020,1021,1022,1023,1036,1037,1038,1039,1040,1041,1044,1045,1046,1047,1048]
arquivo_final.drop(linhas_para_retirar,inplace=True)
arquivo_final.drop(1018,inplace=True)

arquivo_final = arquivo_final[[
    'Corretora', 'Nome_cliente', 'Conta', 'Escritorio', 'UF', 'Assessor',
       'Mesa de Operação', 'Status', 'Exeção', 'Inicio da gestão',
       'Data do distrato', 'Carteira', 'Taxa de gestão',
         'Benchmark','Taxa de performance','Janeiro/2020', 'fereiro/2020', 'Março/2020',
       'Abril/2020', 'Maio/2020', 'junho/2020', 'julho/2020', 'Agosto/2020',
       'Setembro/2020', 'Outubro/2020', 'Novembro/2020', 'Dezembro/2020',
       'Janeiro/2021', 'fereiro/2021', 'Março/2021', 'Abril/2021', 'Maio/2021',
       'junho/2021', 'julho/2021', 'Agosto/2021', 'Setembro/2021',
       'Outubro/2021', 'Dezembro/2021', 'Novembro/2021', 'fereiro/2022',
       'Março/2022', 'Abril/2022', 'Maio/2022', 'junho/2022', 'julho/2022',
       'Agosto/2022', 'Setembro/2022', 'Outubro/2022', 'Novembro/2022',
       'Dezembro/2022', 'Janeiro/2023', 'fereiro/2023',
         'Março/2023', 'Abril/2023', 'Maio/2023',
       'junho/2023', 'julho/2023', 'Agosto/2023', 'Setembro/2023',
       'Outubro/2023'
]]

col_fill_na = ['Janeiro/2020', 'fereiro/2020', 'Março/2020',
       'Abril/2020', 'Maio/2020', 'junho/2020', 'julho/2020', 'Agosto/2020',
       'Setembro/2020', 'Outubro/2020', 'Novembro/2020', 'Dezembro/2020',
       'Janeiro/2021', 'fereiro/2021', 'Março/2021', 'Abril/2021', 'Maio/2021',
       'junho/2021', 'julho/2021', 'Agosto/2021', 'Setembro/2021',
       'Outubro/2021', 'Dezembro/2021', 'Novembro/2021', 'fereiro/2022',
       'Março/2022', 'Abril/2022', 'Maio/2022', 'junho/2022', 'julho/2022',
       'Agosto/2022', 'Setembro/2022', 'Outubro/2022', 'Novembro/2022',
       'Dezembro/2022', 'Janeiro/2023', 'fereiro/2023',
         'Março/2023', 'Abril/2023', 'Maio/2023',
       'junho/2023', 'julho/2023', 'Agosto/2023', 'Setembro/2023',
       'Outubro/2023'
]

for col in col_fill_na:
    arquivo_final[col] = arquivo_final[col].fillna(0)


arquivo_final['Inicio da gestão'] = pd.to_datetime(arquivo_final['Inicio da gestão'],errors='coerce')
arquivo_final['Inicio da gestão'] = arquivo_final['Inicio da gestão'].dt.strftime('%d/%m/%Y')    


arquivo_final['Data do distrato'] = pd.to_datetime(arquivo_final['Data do distrato'],errors='coerce')
arquivo_final['Data do distrato'] = arquivo_final['Data do distrato'].dt.strftime('%d/%m/%Y') 
arquivo_final_copia = arquivo_final.copy()