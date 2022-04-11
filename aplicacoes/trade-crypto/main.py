from binance.client import Client
from secrets import api_secret, api_key
from binance.enums import *

client = Client(api_key=api_secret, api_secret=api_key)

# printando o status da conexao
status = client.get_account_status()
print(status)

# pegar informações da conta
info = client.get_account()
print(info)

# ver saldos dos ativos
print(info['balances'])

# ver ativos que temos na conta
lista_ativos = info['balences']

for ativo in lista_ativos:
    if float(ativo["free"]) > 0:
        print(ativo)

# criar uma ordem de compra dentro da binance
# No caso da compra (SIDE_BUY), BNBBRL significa: comprando BNB usando BRL

order = client.create_order(
    symbol="BNBBRL",
    side=SIDE_BUY,
    type=ORDER_TYPE_MARKET,
    quantity=0.01,
)

print(order)

# criar uma ordem de venda dentro da binance
# No caso da venda (SIDE_BUY), BNBBRL significa: vendendo BNB pra ganhar BRL

order = client.create_order(
    symbol="BNBBRL",
    side=SIDE_SELL,
    type=ORDER_TYPE_MARKET,
    quantity=0.01,
)

print(order)

# visualizar ordens executadas ou em abertas
print(client.get_all_orders(symbol="BNBBRL"))

# visualizar ordens executadas
print(client.get_my_trades(symbol="BNBBRL"))

# mostrar as referencias de cada par moeda
