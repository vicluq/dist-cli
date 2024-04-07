from typer import Typer, Option, Argument
from ..utils.project import is_dist_project
from ..utils.config import add_config
from .create import create_service
from .rename import rename_service
from .delete import delete_service
from .list import list_services
from rich import print as rprint
from typing import Annotated
from rich import print as rprint
from rich.progress import Progress
import os

service_app = Typer(help='Manage services.')

@service_app.command('create', help='Create a service.')
def create(path: Annotated[str, Argument(help='The path to create the service. If src folder is present it will go inside of it.')], 
           name: Annotated[str, Option(help='The service name.', prompt=True)], 
           add_dockerfile: Annotated[bool, Option(help='Include a Dockerfile.', )] = True,
           shared: Annotated[str, Option(help='The shared library.', )] = None):
      is_dist_project() # Check if we are inside an dist Project
      with Progress() as progress:
            task = progress.add_task("[white]Creating service...")

            service_data = create_service(path, name, shared, add_dockerfile, progress, task)
            add_config('services.json', name, service_data)
      
      rprint(f'[green]Service "{name}" created at {service_data['service_path']}[/green]')


@service_app.command('delete', help='Delete a service.')
def delete(name: Annotated[str, Option(help='The service name.', prompt=True)],
            rm: Annotated[bool, Option(help='Wether or not to remove the files.')] = True):
     is_dist_project()
     ok = True
     with Progress() as progress:
            task = progress.add_task("[white]Deleting service...")
            ok = delete_service(name, rm, progress, task)
     if ok:
      rprint(f'[green]Service "{name}" deleted[/green]')


@service_app.command('rename', help='Rename a service.')
def rename(name: Annotated[str, Argument(help='The service current name.')],
           new_name: Annotated[str, Argument(help='The service new name.')]):
      is_dist_project()
      if rename_service(name, new_name):
            rprint(f':thumbsup: [green]Service "{name}" renamed to "{new_name}".[/green]')

@service_app.command('list', help='List the services.')
def list(with_path: Annotated[bool, Option(help='List the services along with the path.')] = True):
     is_dist_project()
     list_services(with_path)