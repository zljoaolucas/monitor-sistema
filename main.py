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

LARGURA = 34

def criar_monitor():
    cpu = ps.cpu_percent(interval=1)
    ram = ps.virtual_memory()
    disco = ps.disk_usage("/")
    rede = ps.net_io_counters()

    enviados = rede.bytes_sent / (1024 * 1024)
    recebidos = rede.bytes_recv / (1024 * 1024)

    tabela = Table(show_header=False, box=None, padding=(0, 0), expand=False)
    tabela.add_column(justify="left")
    tabela.add_column(justify="right")

    tabela.add_row("[dim]CPU[/dim]", f"[{cor(cpu)}]{cpu:>5.1f}%[/{cor(cpu)}]")
    tabela.add_row("[dim]RAM[/dim]", f"[{cor(ram.percent)}]{ram.percent:>5.1f}%[/{cor(ram.percent)}]")
    tabela.add_row("[dim]Disco[/dim]", f"[{cor(disco.percent)}]{disco.percent:>5.1f}%[/{cor(disco.percent)}]")
    tabela.add_row("", "")
    tabela.add_row("[yellow]↑ Envio[/yellow]", f"[yellow]{enviados:>7.1f} MB[/yellow]")
    tabela.add_row("[magenta]↓ Recebido[/magenta]", f"[magenta]{recebidos:>7.1f} MB[/magenta]")

    return Panel(
        tabela,
        title="[bold]Sistema[/bold]",
        title_align="left",
        subtitle="[dim]● live[/dim]",
        subtitle_align="right",
        border_style="cyan",
        box=box.ROUNDED,
        width=LARGURA,
        padding=(0, 1)
    )

def main():
    with Live(
        criar_monitor(),
        refresh_per_second=1,
        screen=False,
        transient=False
    ) as live:
        try:
            while True:
                live.update(criar_monitor())
        except KeyboardInterrupt:
            pass

    console.print("[bold cyan]Monitor encerrado.[/bold cyan]")


if __name__ == "__main__":
    main()