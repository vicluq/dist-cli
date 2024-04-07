from ..utils.config import get_config, delete_config
from rich import print as rprint
import shutil
import os

config_file = 'services.json'

def delete_service(name: str, remove_files: bool, progress, task):
      config = get_config(config_file, name)
      progress.update(task, advance=30)

      if config is None:
            rprint(f'[red]Service "{name}" does not exist.[/red]')
            return False
      
      delete_config(config_file, name)
      progress.update(task, advance=40)

      if remove_files:
            service_path = config['service_path']
            shutil.rmtree(service_path)
      progress.update(task, advance=30)
      
      return True