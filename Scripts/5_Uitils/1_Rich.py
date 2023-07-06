from rich import *
from rich.console import Console

print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

console = Console()

console.print("Hello", "World!")

console.print("Hello", "World!", style="bold red")

console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

