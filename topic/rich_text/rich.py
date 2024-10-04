from rich import * 

'''
Dependency
* markdown_it
  * dmurl
* pygments - syntex hightlight


* www: https://github.com/Textualize/rich
* doc: https://rich.readthedocs.io/en/latest
'''

cnt = 1
# Demo 1 - Rich Print
print (f"[bold blue]Demo {cnt}[/bold blue] - Rich Print")
print ("\tDefine color by tag \[ style ] content \[/ style ]" )
print ("\tMore example: [red]red[/red] [u]u[/u] [i]i[/i]" )
print ("")
cnt = cnt + 1


# Demo 2 - Console

from rich.console import Console

console = Console()
print (f"[bold blue]Demo {cnt}[/bold blue] - console")
console.print("Hello", "World!", style="bold red")
print ("")
cnt = cnt + 1

# Demo - Progress (Basic)

import time
from rich.progress import track

print (f"[bold blue]Demo {cnt}[/bold blue] - Progress (basic)")

for i in track(range(20), description="Processing..."):
    time.sleep(1)  # Simulate work being doneprint ("")

cnt = cnt + 1
