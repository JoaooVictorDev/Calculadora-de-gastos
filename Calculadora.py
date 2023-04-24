import requests
import json


req = None
try:
    req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
    resposta = json.loads(req.text)
    dolar =float(resposta['USDBRL']['high'])
    
except:
    dolar = 5.5 #Preço do Dolar
    print('Erro de Conexao')

def calcular_custo(preco_dolar):
    preco_venda = 0
    preco_reais = float(preco_dolar)*float(dolar)
    comissao = float(preco_venda) * 17/100
    frete_entregador = float(preco_reais)*14/100
    frete_plataforma = 25.00
    custo_total = float(preco_reais)+float(comissao)+float(frete_entregador)+float(frete_plataforma)
    lucro_reais = float(preco_venda) - float(custo_total)
    lucro_porcentagem = float(lucro_reais)*100/float(custo_total)/100

    while lucro_porcentagem <= 0.220:#20% 
        preco_venda = preco_venda + 1
        preco_reais = float(preco_dolar)*float(dolar)
        comissao = float(preco_venda) * 17/100
        frete_entregador = float(preco_reais)*14/100
        frete_plataforma = 25.00
        custo_total = float(preco_reais)+float(comissao)+float(frete_entregador)+float(frete_plataforma)
        lucro_reais = float(preco_venda) - float(custo_total)
        lucro_porcentagem = float(lucro_reais)*100/float(custo_total)/100

    return preco_venda

print(calcular_custo(245))