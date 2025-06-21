import requests
import pandas as pd
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": "false"
}
resposta = requests.get(url, params=params)

if resposta.status_code == 200:

    df = pd.DataFrame(resposta.json())

    print("\n MOEDAS MAIS CARAS(maior que 1000 dolares)\n ")
    moedas_caras = df[df['current_price'] > 1000][['current_price','name','symbol']].sort_values(by='current_price',ascending=False)
    print(moedas_caras)

    print("\n AS 10 MOEDAS COM MAIOR VOLUME DE NEGOCIAÇÃO NAS ULTIMAS 24H \n")
    volume =df[['name','total_volume']]
    volume_dez = volume.head(10)
    print(volume_dez)

    print("\n MOEDAS QUE SUBIRAM MAIS DE 5% NAS ULTTIMAS 24H \n")
    porcentagem = df[df['price_change_percentage_24h']> 5][['name','price_change_percentage_24h']].sort_values(by='price_change_percentage_24h',ascending=False)
    print(porcentagem)

    moedas_caras.to_csv("MOEDAS MAIS CARAS.csv", index=False)
    volume_dez.to_csv("AS 10 MOEDAS COM MAIOR VOLUME DE NEGOCIAÇÃO NAS ULTIMAS 24H.csv", index=False)
    porcentagem.to_csv("MOEDAS QUE SUBIRAM MAIS DE 5% NAS ULTTIMAS 24H.csv", index=False)
    
else:
    print("Erro na requisição:", resposta.status_code)
