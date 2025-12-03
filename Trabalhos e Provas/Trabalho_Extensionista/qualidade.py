import pandas as pd
from graficos import scatterplot_gastos, boxplot_gastos

deputados = pd.read_excel("planilhas/deputados.xlsx")
gastos = pd.read_excel("planilhas/gastos.xlsx")

def limpeza_dados(df):
    print("\nDados antes da limpeza:")
    print(df.info())

    # Identifica colunas com pelo menos um valor ausente
    colunas_com_na = df.columns[df.isnull().any()].tolist()

    # Remove linhas com valores ausentes
    gastos_limpos = df.dropna(subset=colunas_com_na)

    # Remove linhas com valores negativos em todas as colunas numéricas
    cols_numericas = gastos_limpos.select_dtypes(include='number').columns
    for col in cols_numericas:
        gastos_limpos = gastos_limpos[gastos_limpos[col] >= 0]

    # Remove linhas com ano fora do intervalo 2018-2022
    if 'Data' in gastos_limpos.columns:
        datas = pd.to_datetime(gastos_limpos['Data'], format="%d/%m/%Y %H:%M", errors='coerce')
        anos_validos = (datas.dt.year >= 2018) & (datas.dt.year <= 2022)
        gastos_limpos = gastos_limpos[anos_validos]

    print("\nDados após limpeza:")
    print(gastos_limpos.info())

    # Quantidade de linhas removidas
    linhas_removidas = len(df) - len(gastos_limpos)
    print(f"\nQuantidade de linhas removidas: {linhas_removidas}")

    return gastos_limpos

if __name__ == "__main__":
    gastos_limpos = limpeza_dados(gastos)

    scatterplot_gastos(gastos_limpos)
    boxplot_gastos(gastos_limpos)