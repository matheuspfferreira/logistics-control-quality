import csv
from random import randint, choice
from datetime import datetime, timedelta

transportadoras = [
    "TR001", "TR002", "TR003", "TR004", "TR005", "TR006",
    "TR007", "TR008", "TR009", "TR010", "TR011", "TR012"
]

cidades_brasil = [
    "São Paulo, SP", "Rio de Janeiro, RJ", "Belo Horizonte, MG", "Brasília, DF",
    "Salvador, BA", "Fortaleza, CE", "Curitiba, PR", "Manaus, AM",
    "Recife, PE", "Porto Alegre, RS", "Goiânia, GO", "Belém, PA",
    "Campinas, SP", "São Luís, MA", "Maceió, AL", "Duque de Caxias, RJ",
    "Nova Iguaçu, RJ", "Natal, RN", "Teresina, PI", "São Bernardo do Campo, SP",
    "Campo Grande, MS", "Jaboatão dos Guararapes, PE", "Osasco, SP", "Santo André, SP",
    "João Pessoa, PB", "Ribeirão Preto, SP", "Uberlândia, MG", "Contagem, MG",
    "Aracaju, SE", "Feira de Santana, BA", "Cuiabá, MT", "Joinville, SC",
    "Londrina, PR", "Niterói, RJ", "São José dos Campos, SP", "Ananindeua, PA",
    "Belford Roxo, RJ", "Caxias do Sul, RS", "Vila Velha, ES", "Serra, ES"
]

def random_date(start, end):
    delta = end - start
    random_days = randint(0, delta.days)
    return start + timedelta(days=random_days)

num_registros = 1202
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

registros = []
for i in range(1, num_registros + 1):
    id_transp = choice(transportadoras)
    data_pedido = random_date(start_date, end_date)
    
    data_previsao_entrega = data_pedido + timedelta(days=randint(1, 7))
    
    data_entrega = data_previsao_entrega + timedelta(days=randint(0, 3))
    
    cidade_origem = choice(cidades_brasil)
    cidade_destino = choice([c for c in cidades_brasil if c != cidade_origem])
    
    registros.append({
        "Id": i,
        "IdTransportadora": id_transp,
        "DataPedido": data_pedido.strftime("%Y-%m-%d"),
        "DataPrevisaoEntrega": data_previsao_entrega.strftime("%Y-%m-%d"),
        "DataEntrega": data_entrega.strftime("%Y-%m-%d"),
        "CidadeOrigem": cidade_origem,
        "CidadeDestino": cidade_destino
    })

with open('data-delivery.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=registros[0].keys())
    writer.writeheader()
    writer.writerows(registros)

print("Arquivo 'data-delivery.csv' criado com sucesso")
