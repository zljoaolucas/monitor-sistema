import psutil as ps
from rich import box
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.table import Table

console = Console()

def cor(valor):
    if valor > 80:
        return "red"
    elif valor > 50:
        return "yellow"
    return "green"

def criar_monitor():
    cpu = ps.cpu_percent(interval=1)
    ram = ps.virtual_memory()
    disco = ps.disk_usage("/")

    rede = ps.net_io_counters()

    enviados = rede.bytes_sent / (1024 * 1024)
    recebidos = rede.bytes_recv / (1024 * 1024)

    tabela = Table(
        show_header=False,
        box=None,
        expand=True,
        padding=(0, 2)
    )

    tabela.add_column("CPU", justify="center")
    tabela.add_column("RAM", justify="center")
    tabela.add_column("DISCO", justify="center")

    tabela.add_row(
        f"[bold]CPU[/bold]\n"
        f"[{cor(cpu)}]{cpu:.1f}%[/{cor(cpu)}]",

        f"[bold]RAM[/bold]\n"
        f"[{cor(ram.percent)}]{ram.percent:.1f}%[/{cor(ram.percent)}]",

        f"[bold]DISCO[/bold]\n"
        f"[{cor(disco.percent)}]{disco.percent:.1f}%[/{cor(disco.percent)}]"
    )

    tabela.add_row(
        f"[dim]{ram.used // (1024**2)} MB usados[/dim]",
        f"[dim]{ram.available // (1024**2)} MB disponíveis[/dim]",
        f"[dim]{disco.free // (1024**3)} GB livres[/dim]"
    )

    tabela.add_row("", "", "")

    tabela.add_row(
        "[yellow]↑ Enviado[/yellow]",
        "[magenta]↓ Recebido[/magenta]",
        ""
    )

    tabela.add_row(
        f"[yellow]{enviados:.2f} MB[/yellow]",
        f"[magenta]{recebidos:.2f} MB[/magenta]",
        ""
    )

    return Panel(
        tabela,
        title="[bold]Resumo de Recursos[/bold]",
        subtitle="[dim]Dados via psutil[/dim]",
        border_style="cyan",
        box=box.ROUNDED,
        padding=(1, 2)
    )

def tela():
    tabela = Table(
        show_header=False,
        box=None,
        expand=True
    )

    tabela.add_column()

    tabela.add_row(
        Panel(
            "[bold white on blue] MONITOR DE SISTEMA EM TEMPO REAL [/bold white on blue]"
            " [bold green]● ONLINE[/bold green]",
            border_style="cyan",
            box=box.ROUNDED
        )
    )

    tabela.add_row(criar_monitor())

    return tabela

def main():
    with Live(
        tela(),
        refresh_per_second=1,
        screen=True
    ) as live:
        try:
            while True:
                live.update(tela())
        except KeyboardInterrupt:
            pass

    console.print("\n[bold cyan]Monitor encerrado.[/bold cyan]")

if __name__ == "__main__":
    main()