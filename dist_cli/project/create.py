from rich import print as rprint
import json
import os

def create_project(name: str, src_folder: bool, progress, task):
      if os.path.exists(name):
            rprint(f'[red bold]Directory {name} already exists.[/red bold]')
            return False
      
      progress.update(task, advance=25)

      os.makedirs(name)
      os.mkdir(f'{name}/.dist')
      os.mkdir(f'{name}/tests')
      progress.update(task, advance=25)

      if src_folder:
            os.mkdir(f'{name}/src')
      
      with open(f'{name}/.env', 'w') as f:
            f.close()
      progress.update(task, advance=25)
      
      # Adding config.json
      with open(f'{name}/.dist/config.json', 'w') as f:
            config = {
                  'project_name': name,
                  'version': '0.1.0',
                  'authors': [],
                  'src': src_folder,
            }
            f.write(json.dumps(config))
            f.close()
      progress.update(task, advance=25)

      return True