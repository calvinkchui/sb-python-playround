from rich.prompt import Prompt

'''
doc: https://rich.readthedocs.io/en/latest/prompt.html
'''

cnt = 1

# Demo - Prompt
print (f"[bold blue]Demo {cnt}[/bold blue] - Prompt")
name = Prompt.ask("Enter your name")
print ("\tenter", name)
print ("")

# Demo - Prompt (Choice)
print (f"[bold blue]Demo {cnt}[/bold blue] - Choice")
name = Prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul")
print ("\tenter", name)
print ("")

from rich.prompt import IntPrompt
from rich.prompt import FloatPrompt
print (f"[bold blue]Demo {cnt}[/bold blue] - IntPrompt.ask")
ni = IntPrompt.ask("Enter an integer?")
print ("\tenter", ni)
print ("")

print (f"[bold blue]Demo {cnt}[/bold blue] - FloatPrompt.ask")
nf = FloatPrompt.ask("Enter an float?")
print ("\tenter", nf)
print ("")

# Demo - Prompt (Confirm)
from rich.prompt import Confirm

print (f"[bold blue]Demo {cnt}[/bold blue] - Confirm .ask")
is_rich_great = Confirm.ask("Do you like rich?")
print ("\tenter", is_rich_great)
print ("")



