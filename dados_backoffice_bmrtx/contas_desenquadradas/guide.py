import pandas as pd
import streamlit as st
import openpyxl
import numpy as np
import plotly.graph_objects as pgo
import base64
from io import BytesIO
import io
import xlsxwriter as xlsxwriter



class Contas_desenquadradas():
        def __init__(self):
            print('hello')
            
        def manipulado_pl_guide(self,df,daf):

                pl = df#pd.read_excel(r'C:\Users\lauro.telles\Desktop\Projeto app Backoffice\PL Janeiro.xlsx')        
                controle = daf#pd.read_excel(r'C:\Users\lauro.telles\Desktop\Projeto app Backoffice\Controle de Contratos - Atualizado Fevereiro de 2024 (4).xlsx',3,skiprows=1).iloc[:,[1,2,4,5,7,8,12,-1]]

                patrimio_liquido = pl[['CLIE_ID','SALDO_BRUTO']].groupby('CLIE_ID')['SALDO_BRUTO'].sum().reset_index().rename(columns={'CLIE_ID':'Conta',
                                                                                                                                                    'SALDO_BRUTO':'PL Total Atual'}).reset_index(drop='index')
                patrimio_liquido['Conta'] = patrimio_liquido['Conta'].astype(str)
                controle['Conta'] = controle['Conta'].str[:-1]

                self.arquivo_final = pd.merge(patrimio_liquido,controle, on='Conta',how='outer')
                self.arquivo_final = self.arquivo_final[self.arquivo_final['Situação']!='Monitoramento']
                self.arquivo_final = self.arquivo_final.loc[(self.arquivo_final['Status']=='Ativo')|(self.arquivo_final['Status']=='Inativo')]
                
                return self.arquivo_final
        def filtro_pl_100(self,arquivo_final):
                
                self.filtro_pl_abaixo_100k = arquivo_final.loc[arquivo_final['PL Total Atual']<1000].reset_index(drop=True)
                return self.filtro_pl_abaixo_100k
        
        def income(self,arquivo_final):
                self.filtro_income = arquivo_final.loc[
                    (arquivo_final['Carteira']== 'INC') & (arquivo_final['PL Total Atual']<60000)].reset_index(drop=True)
                return self.filtro_income
        def income_abaixo_100(self,arquivo_final):
                self.filtro_abaixo100k_e_income = arquivo_final.loc[
                    (arquivo_final['Carteira']!='INC')&(arquivo_final['PL Total Atual']<100000)&(arquivo_final['Carteira']!='FUND')].reset_index(drop=True)
                return self.filtro_abaixo100k_e_income
        def pl_0(self,arquivo_final):
                self.filtro_pl_0 = arquivo_final[arquivo_final.iloc[:,-1]<1].reset_index(drop=True)
                return self.filtro_pl_0
    
class Btg_contas_desenquadradas():
        def __init__(self):
                print('hello')

        def manipulando_pl_BTG(self,df,daf):
               
                pl = df
                controle = daf

                controle = controle.iloc[:,[1,2,4,5,8,12,-2,7]]

                
                pl['Conta'] = pl['Conta'].astype(str)
                pl['Conta'] = list(map(lambda x: x[2:], pl['Conta']))
        
                controle['Conta']=controle['Conta'].astype(str).str[:-2]
                controle['Conta'] = controle['Conta'].astype(str)
                pl = pl.rename(columns={'Valor':'PL', 'Nome':'Nome do cliente pelo excel PL'})
        
                pl=pl[['Conta','Nome do cliente pelo excel PL','PL']]
        

                self.arquivo_final = pd.merge(controle,pl,on='Conta',how='outer')
                self.arquivo_final = self.arquivo_final[self.arquivo_final['Situação']!='Monitoramento']
                self.arquivo_final = self.arquivo_final.loc[(self.arquivo_final['Status']=='Ativo')|(self.arquivo_final['Status']=='Inativo')]
                self.arquivo_final = self.arquivo_final.drop(columns=['Nome do cliente pelo excel PL','Status'])
                return self.arquivo_final
                
        def filtrando_pl_100(self,arquivo_final):
                self.filtro_pl_abaixo_100k = arquivo_final.loc[arquivo_final.PL<1000].reset_index(drop=True)
                return self.filtro_pl_abaixo_100k
        
        def income_btg(self,arquivo_final):
                self.filtro_income = arquivo_final.loc[(arquivo_final['Carteira']== 'INC') & (arquivo_final.PL<60000)].reset_index(drop=True)
                return self.filtro_income
        def cemk_e_income(self,arquivo_final):
                self.filtro_abaixo100k = arquivo_final.loc[(arquivo_final['Carteira']!='INC')&(arquivo_final['PL']<100000)&(arquivo_final['Carteira']!='FUND')].reset_index(drop=True)
                return self.filtro_pl_abaixo_100k
        def pl_zerado_btg(self,arquivo_final):
                self.filtro_pl_0_btg = arquivo_final[arquivo_final.iloc[:,-2]<1].reset_index(drop=True)
                return self.filtro_pl_0_btg


# if __name__=='__main__':
        
#     teste = Contas_desenquadradas()
#     arquivo_final = teste.manipulado_pl_guide(df,daf)
#     pl_0 = teste.pl_0(arquivo_final)
#     filtro_pl_abaixo_100k = teste.income_abaixo_100(arquivo_final)
#     filtro_income = teste.income(arquivo_final)
#     filtro_abaixo100k = teste.filtro_pl_100(arquivo_final)

#     st.subheader('Contas com valor de PL abaixo de R$100.000,00')
#     st.dataframe(filtro_abaixo100k)
#     st.subheader('Contas Income com PL abaixo de R$60.000,00')
#     st.dataframe(filtro_income)
#     st.subheader('Contas com valor de PL abaixo de R$1000,00')
#     st.dataframe(filtro_pl_abaixo_100k)
#     st.subheader('Contas zeradas partindo da planilha de controle')
#     st.dataframe(pl_0)
#     # st.dataframe(arquivo_final)




