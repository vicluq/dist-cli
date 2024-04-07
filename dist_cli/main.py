from typer import Typer, Argument, Option
from .service.main import service_app
from typing import Annotated
from rich import print as rprint
from .project.create import create_project
from rich.progress import Progress

app = Typer(name='dist-cli')
app.add_typer(service_app, name='service')


@app.command('init', help='Starts a dist Project')
def init(name: Annotated[str, Argument(help='The project name.')],
         src_folder: Annotated[bool, Option(help='Add a src folder as the code placement.')] = True):
      ok = True
      with Progress() as progress:
            task = progress.add_task("[white]Creating the project...")
            ok = create_project(name, src_folder, progress, task)
      if ok:
            rprint(f':white_heavy_check_mark: [green bold]Project created[/green bold]')
            rprint(f'cd {name}')

if __name__ == '__main__':
      app()