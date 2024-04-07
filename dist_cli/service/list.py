from ..utils.config import get_all_config
from rich.table import Table
from rich.console import Console

def list_services(with_path: bool):
      services = get_all_config('services.json')

      table = Table(title='Services', highlight=True, leading=True)
      table.add_column("Name", justify="left", style="cyan", no_wrap=True)
      
      if with_path:
            table.add_column("Path", justify="left", style="green", no_wrap=True)

      for k, v in services.items():
            row = [k] + ([v['service_path']] if with_path else [])
            table.add_row(*row)
            
      console = Console()
      console.print(table)