from typer import Exit
from rich import print as rprint
import os

def is_dist_project():
      ok = os.path.exists('.dist/config.json')
      if not ok:
            rprint(f'[red bold]Not a Dist project[/red bold]')
            raise Exit()
      return