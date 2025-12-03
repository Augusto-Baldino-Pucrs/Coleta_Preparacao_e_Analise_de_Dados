from deputados import gerar_planilha as get_deputados
from gastos_ano import gerar_planilha as get_gastos
from rich.console import Console
console = Console()

def main():
    console.rule("[bold yellow]Seção 1 - Deputados[/bold yellow]")
    console.print("[bold blue]Iniciando a coleta de dados dos deputados...[/bold blue]")
    get_deputados()
    console.print("[green]Planilha de deputados gerada com sucesso![/green]")

    console.rule("[bold yellow]Seção 2 - Gastos[/bold yellow]")
    console.print("[bold blue]Iniciando a coleta de dados dos gastos...[/bold blue]")
    get_gastos()
    console.print("[green]Planilha de gastos gerada com sucesso![/green]")

if __name__ == "__main__":
    main()