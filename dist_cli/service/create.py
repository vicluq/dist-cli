from rich import print as rprint
from ..templates.microservices import get_logic_template, get_main_template
from ..utils.config import get_config
import pathlib
import os


def create_service(path: str, name: str, shared: str, add_dockerfile: bool, progress, task):
      # Getting config
      is_src = get_config('config.json', 'src')

      current_dir = os.path.dirname(os.path.abspath(__file__))

      path = f'{'src/' if is_src else ''}{path}'

      base_path = pathlib.Path(path)
      if not base_path.exists():
            os.mkdir(base_path.absolute())
      
      progress.update(task, advance=10)

      service_path = pathlib.Path(f'{path}/{name}')
      if service_path.exists():
            rprint(f'[red]Service "{name}" already exists.[/red]')
      
      if shared:
            shared_path = pathlib.Path(shared)
            shared_packages = os.listdir(shared)

      progress.update(task, advance=30)

      # Creating the service structure
      os.mkdir(service_path.absolute())
      src = pathlib.Path(f'{service_path.absolute()}/src')
      src.mkdir()

      if add_dockerfile:
            template = open(f'{current_dir}/../templates/Dockerfile-python')
            docker_f = open(f'{service_path.absolute()}/Dockerfile', mode='w')
            docker_f.write(template.read())
            docker_f.close()
            template.close()

      progress.update(task, advance=10)

      with open(f'{src.absolute()}/main.py', 'w') as file:
            file.write(get_main_template(name))
            file.close()
      progress.update(task, advance=10)
      
      # TODO: add template with shared repositories
      with open(f'{src.absolute()}/setup.py', 'w') as file:
            file.close()
      progress.update(task, advance=10)


      serv = pathlib.Path(f'{src.absolute()}/service')
      serv.mkdir()

      with open(f'{serv.absolute()}/logic.py', 'w') as file:
            file.write(get_logic_template(name))
            file.close()
      progress.update(task, advance=30)

      return {
            'base_path': base_path.absolute().as_posix(),
            'service_path': service_path.absolute().as_posix(),
            'shared': shared_path.absolute().as_posix() if shared else None
      }
      