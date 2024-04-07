from ..utils.config import update_config, get_config
from rich import print as rprint
import os

def rename_service(name: str, new_name: str):
      service = get_config('services.json', name)
      if not service:
            rprint(f':x: [red]Service does not exist.[/red]')

      new_service_path = f'{service['base_path']}/{new_name}'
      os.rename(service['service_path'], new_service_path)

      new_data = dict(service)
      new_data['service_path'] = new_service_path
      
      if update_config('services.json', name, new_data, new_name):
            return True
      else:
            rprint(f':thumbsdown: [red]Service "{name}" could not be renamed. Check if the name is valid as a directory name.[/red]')