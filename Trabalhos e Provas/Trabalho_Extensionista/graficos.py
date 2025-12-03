import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

deputados = pd.read_excel("planilhas/deputados.xlsx")
gastos = pd.read_excel("planilhas/gastos.xlsx")

def scatterplot_gastos(df_gastos):
    # Converter a coluna 'Data' para datetime
    df_gastos['Data'] = pd.to_datetime(df_gastos['Data'], format="%d/%m/%Y %H:%M", errors='coerce')

    # Calcular a correlação entre 'Valor (R$)' e 'Data'
    correlacao_gastos_ano = df_gastos['Valor (R$)'].corr(df_gastos['Data'].astype('int64'))
    print(f"Correlação entre 'Valor' e 'Data': {correlacao_gastos_ano}")

    # Scatter plot dos gastos ao longo do tempo
    sns.scatterplot(data=df_gastos, x="Data", y="Valor (R$)")
    plt.gca().xaxis.set_major_locator(mdates.YearLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    plt.gcf().autofmt_xdate() 
    plt.title("Distribuição dos gastos por ano")
    plt.show()

def boxplot_gastos(df_gastos):
    # O eixo X do boxplot deve ser categórico
    if 'Ano' not in df_gastos.columns:
        df_gastos['Ano'] = pd.to_datetime(df_gastos['Data'], format="%d/%m/%Y %H:%M", errors='coerce').dt.year
    df_gastos['Ano'] = df_gastos['Ano'].astype('Int64')

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df_gastos, x="Ano", y="Valor (R$)")
    plt.title("Boxplot dos gastos por ano")
    plt.xlabel("Ano")
    plt.ylabel("Valor (R$)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    scatterplot_gastos(gastos)
    #boxplot_gastos(gastos)