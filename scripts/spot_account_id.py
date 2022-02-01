import click
import json

from spotinst_sdk2 import SpotinstSession


@click.group()
@click.pass_context
def cli(ctx, *args, **kwargs):
    ctx.obj = {}


@cli.command()
@click.option(
    '--filter',
    required=False,
    help='Return matching records. Syntax: key=value'
)
@click.option(
    '--attr',
    required=False,
    help='Return only the raw value of a single attribute'
)
@click.option(
    '--token',
    required=False,
    help='Spotinst Token'
)
@click.pass_context
def get(ctx, *args, **kwargs):
    """Returns ONLY the first match"""
    session = SpotinstSession(auth_token=kwargs.get('token'))
    ctx.obj['client'] = session.client("admin")
    result = ctx.obj['client'].get_accounts()
    if kwargs.get('filter'):
        k, v = kwargs.get('filter').split('=')
        result = [x for x in result if x[k] == v]
    if kwargs.get('attr'):
        if result:
            if result[0].get(kwargs.get('attr')):
                click.echo(result[0].get(kwargs.get('attr')))
            else:
                fail_string = {'account_id': ''}
                click.echo(json.dumps(fail_string))
        else:
            fail_string = {'account_id': ''}
            click.echo(json.dumps(fail_string))
    else:
        if result:
            click.echo(json.dumps(result[0]))
        else:
            fail_string = {'account_id': ''}
            click.echo(json.dumps(fail_string))


if __name__ == "__main__":
    cli()
