import json
from openpyxl import Workbook
from datetime import datetime

gastos = []

def ler_arquivo(ano):
    with open(f'arquivos/{ano}.json', encoding='utf-8') as f:
        data = json.load(f)
        processar_dados(data)

def processar_dados(data):
    for i in data['dados']:
        id = i.get('idDeputado')
        if id is None:
            continue

        nome = i['nomeParlamentar'].title()

        descricao = i.get('descricao', 'N/A').title()

        fornecedor = i.get('fornecedor', 'N/A').title()

        data_raw = i.get('dataEmissao', 'N/A')
        if data_raw != 'N/A':
            try:
                data_hora = datetime.strptime(data_raw, "%Y-%m-%dT%H:%M:%S").strftime("%d/%m/%Y %H:%M")
            except ValueError:
                data_hora = data_raw
        else:
            data_hora = 'N/A'

        valor_raw = i.get('valorLiquido', 0)
        try:
            valor = float(valor_raw)
        except (TypeError, ValueError):
            continue

        gastos.append({
            "id": id,
            "nome": nome,
            "descricao": descricao,
            "fornecedor": fornecedor,
            "data": data_hora,
            "valor": valor
        })

def get_gastos():
    for ano in range(2018, 2023):
        ler_arquivo(ano)

    return gastos

def gerar_planilha():
    gastos = get_gastos()

    wb = Workbook()
    ws = wb.active
    ws.title = "Gastos"
    ws.append(["ID", "Nome", "Descrição", "Fornecedor", "Data", "Valor (R$)"])

    for gasto in gastos:
        ws.append([
            gasto["id"],
            gasto["nome"],
            gasto["descricao"],
            gasto["fornecedor"],
            gasto["data"],
            gasto["valor"]
        ])

    wb.save("planilhas/gastos.xlsx")

if __name__ == "__main__":
    gerar_planilha()