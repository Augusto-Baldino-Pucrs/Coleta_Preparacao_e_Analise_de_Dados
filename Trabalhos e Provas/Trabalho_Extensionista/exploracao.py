import pandas as pd

def geral(deputados, gastos):
    # Primeiras e últimas linhas
    print("Primeiras linhas do DataFrame 'deputados':")
    print(deputados.head())
    print("\nÚltimas linhas do DataFrame 'deputados':")
    print(deputados.tail())

    print("\nPrimeiras linhas do DataFrame 'gastos':")
    print(gastos.head())
    print("\nÚltimas linhas do DataFrame 'gastos':")
    print(gastos.tail())

    # Dimensões
    print("\nDimensões do DataFrame 'deputados':", deputados.shape)
    print("Dimensões do DataFrame 'gastos':", gastos.shape)

    # Nomes
    print("Nomes das colunas do DataFrame 'deputados':", deputados.columns.tolist())
    print("Nomes das colunas do DataFrame 'gastos':", gastos.columns.tolist())

    # Informações gerais
    print("\nInformações gerais do DataFrame 'deputados':")
    deputados.info()

    print("\nInformações gerais do DataFrame 'gastos':")
    gastos.info()

def estatisticas(deputados, gastos):
    # Estatísticas descritivas
    print("\nEstatísticas descritivas do DataFrame 'deputados':")
    print(deputados.describe())

    print("\nEstatísticas descritivas do DataFrame 'gastos':")
    print(gastos.describe())

    # Estatísticas gerais
    print("\nEstatísticas gerais do DataFrame 'deputados':")
    print(deputados.describe(include='all'))

    print("\nEstatísticas gerais do DataFrame 'gastos':")
    print(gastos.describe(include='all'))

    # Contagem de valores únicos por coluna
    print("\nContagem de valores únicos por coluna no DataFrame 'deputados':")
    print(deputados.nunique())

    print("\nContagem de valores únicos por coluna no DataFrame 'gastos':")
    print(gastos.nunique())

    # Contagem de valores por coluna
    print("\nContagem de valores por coluna no DataFrame 'deputados':")
    for col in deputados.columns:
        print(f"\nColuna: {col}")
        print(deputados[col].value_counts().head())

    print("\nContagem de valores por coluna no DataFrame 'gastos':")
    for col in gastos.columns:
        print(f"\nColuna: {col}")
        print(gastos[col].value_counts().head())

if __name__ == "__main__":
    deputados = pd.read_excel("planilhas/deputados.xlsx")
    gastos = pd.read_excel("planilhas/gastos.xlsx")

    geral(deputados, gastos)
    estatisticas(deputados, gastos)