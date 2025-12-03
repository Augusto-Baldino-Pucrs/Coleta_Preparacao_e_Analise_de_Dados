import requests
from openpyxl import Workbook

# URL da API para obter os deputados da 56ª legislatura
url = "https://dadosabertos.camara.leg.br/api/v2/deputados?idLegislatura=56&ordem=ASC&ordenarPor=nome"

def obter_deputados(url):
    deputados = {}
    while url:
        response = requests.get(url)
        if response.status_code != 200:
            print("Erro ao acessar a API:", response.status_code)
            break

        data = response.json()
        for deputado in data['dados']:
            deputados[deputado['id']] = {
                'id': deputado['id'],
                # Normalizar nome do deputado
                'nome': deputado['nome'].title(),
                'partido': deputado['siglaPartido'],
                'estado': deputado['siglaUf'],
                'legislatura': deputado['idLegislatura']
            }

        url = proxima_pagina(data)
    return deputados

def proxima_pagina(data):
    # Verifica se há um link para a próxima página
    for link in data.get('links', []):
        if link.get('rel') == 'next':
            return link.get('href')
    return None

def gerar_planilha():
    deputados = obter_deputados(url)

    wb = Workbook()
    ws = wb.active
    ws.title = "Deputados"
    ws.append(["ID", "Nome", "Partido", "Estado", "Legislatura"])

    for id, info in deputados.items():
        ws.append([
            info["id"],
            info["nome"],
            info["partido"],
            info["estado"],
            info["legislatura"]
        ])

    wb.save("planilhas/deputados.xlsx")

if __name__ == "__main__":
    gerar_planilha()