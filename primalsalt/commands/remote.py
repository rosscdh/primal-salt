import os
import sys
import click
from pathlib import Path
from services import PushProjectFromConfigService
cwd = os.getcwd()


@click.group()
@click.pass_context
def remote(ctx):
    pass


@remote.command()
@click.option('--path', prompt='path to existing primal.yml', help='Your existing primal.yml file')
@click.pass_context
def push(ctx, path):
    """Command on cli1"""
    file = Path(path)
    directory = file.parent

    if file.exists() is False:
        click.ClickException('{} is not a file. (primal.yml)'.format(path)).show()
        sys.exit()

    if click.confirm('Load {} and push primal salt project at: {}'.format(path, directory)):
        service = PushProjectFromConfigService(config_file=file)
        config = service.push()
        click.echo(config)
