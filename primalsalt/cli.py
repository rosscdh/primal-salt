import click

from commands.project import project
from commands.remote import remote


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.obj['DEBUG'] = debug


cli.add_command(project)
cli.add_command(remote)


def run():
    cli(obj={})


if __name__ == '__main__':
    run()
