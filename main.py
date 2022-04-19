import pandas as pd
from twilio.rest import Client
# Minha conta SID
account_sid = "AC1fc31f00b38482595ff700e8f93944f5"
# Meu Auth Token
auth_token  = "d53c7c1f602f848f326edecd87200596"
client = Client(account_sid, auth_token)

lmeses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lmeses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor:{vendedor} - Vendas:{vendas}')
