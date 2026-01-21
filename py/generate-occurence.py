import csv
from random import randint, choice
from datetime import datetime, timedelta

tipos_ocorrencia = ["Atraso", "Avaria", "Extravio"]

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

def random_date(start, end):
    delta = end - start
    random_days = randint(0, delta.days)
    return start + timedelta(days=random_days)

num_ocorrencias = 451
registros = []

for i in range(1, num_ocorrencias + 1):
    id_entrega = randint(1, 1202)
    tipo = choice(tipos_ocorrencia)
    data = random_date(start_date, end_date)
    registros.append({
        "Id": i,
        "IdEntrega": id_entrega,
        "Tipo": tipo,
        "Data": data.strftime("%Y-%m-%d")
    })

# Criar arquivo CSV
with open("data-occurence.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Id", "IdEntrega", "Tipo", "Data"])
    writer.writeheader()
    writer.writerows(registros)

print("Arquivo 'data-occurence.csv' criado com sucesso")
