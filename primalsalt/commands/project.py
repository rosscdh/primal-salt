import os
import sys
import click
from pathlib import Path
from services import ConfigLoaderService, ConfigCreatorService, BuildProjectFromConfigService
cwd = os.getcwd()


@click.group()
@click.pass_context
def project(ctx):
    pass


@project.command()
@click.option('--path', default=cwd, help='The path to the directory for this new primalsalt project')
@click.pass_context
def init(ctx, path):
    """ """
    directory = Path(path)

    if directory.is_dir() is False:
        click.ClickException('{} is not a directory.'.format(path)).show()
        sys.exit()

    if click.confirm('You want to start a new primal salt project at: {}'.format(directory)):
        config_create_service = ConfigCreatorService(path=directory)
        config_create_service.create()
        build_service = BuildProjectFromConfigService(config_file=config_create_service.config_file)
        build_service.build()
        build_service.build_formulas()
        build_service.build_pillars()
        build_service.build_profiles()


@project.command()
@click.option('--path', prompt='path to existing primal.yml', help='Your existing primal.yml file')
@click.pass_context
def load(ctx, path):
    """Command on cli1"""
    file = Path(path)
    directory = file.parent

    if file.exists() is False:
        click.ClickException('{} is not a file. (primal.yml)'.format(path)).show()
        sys.exit()

    if click.confirm('Load {} and create a primal salt project at: {}'.format(path, directory)):
        service = ConfigLoaderService(config_file=file)
        config = service.load()
        click.echo(config)
