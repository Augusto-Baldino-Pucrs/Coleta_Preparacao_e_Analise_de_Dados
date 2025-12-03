import pandas as pd
from tabulate import tabulate

deputados = pd.read_excel("planilhas/deputados.xlsx")
gastos = pd.read_excel("planilhas/gastos.xlsx")

deputados_info = pd.DataFrame({
    "Coluna": deputados.columns,
    "Tipo de dado": [str(deputados[col].dtype) for col in deputados.columns],
    "Exemplo": [deputados[col].dropna().iloc[0] if deputados[col].notna().any() else "" for col in deputados.columns]
})

gastos_info = pd.DataFrame({
    "Coluna": gastos.columns,
    "Tipo de dado": [str(gastos[col].dtype) for col in gastos.columns],
    "Exemplo": [gastos[col].dropna().iloc[0] if gastos[col].notna().any() else "" for col in gastos.columns]
})

print("Informações sobre o DataFrame 'deputados':")
print(tabulate(deputados_info, headers='keys', tablefmt='grid'))

print("\nInformações sobre o DataFrame 'gastos':")
print(tabulate(gastos_info, headers='keys', tablefmt='grid'))