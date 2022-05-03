import pandas as pd
from twilio.rest import Client

accSid = "ur sid acc code"
auth_token  = "ur auth token code"
client = Client(accSid, auth_token)

lmonths = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']

for month in lmonths:
    sales_table = pd.read_excel(f'{month}.xlsx')
    if (sales_table['Vendas'] > 55000).any():
        saller = sales_table.loc[sales_table['Vendas'] > 55000, 'Vendedor'].values[0]
        sales = sales_table.loc[sales_table['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {month} alguém bateu a meta. Vendedor:{saller} - Vendas:{sales}')
        message = client.messages.create(
                    to="number wt area code",
                    from_="ur code here",
                    body=f"No mês de {month} alguém bateu a meta. Vendedor:{saller} - Vendas:{sales}")
        print(message.sid)