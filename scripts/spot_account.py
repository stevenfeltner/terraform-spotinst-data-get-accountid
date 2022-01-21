import click
import json
import requests
import base64
import re
import os

from spotinst_sdk2 import SpotinstSession

token_val = os.environ.get('SPOTINST_TOKEN')

@click.group()
@click.pass_context
def cli(ctx, *args, **kwargs):
    ctx.obj = {}
    session = SpotinstSession()
    ctx.obj['client'] = session.client("admin")


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
@click.pass_context
def get(ctx, *args, **kwargs):
    """Returns ONLY the first match"""
    ctx.obj['client'].account_id = kwargs.get('account_id')
    result = ctx.obj['client'].get_accounts()
    if kwargs.get('filter'):
        k, v = kwargs.get('filter').split('=')
        result = [x for x in result if x[k] == v]
    if kwargs.get('attr'):
        if result:
            result = result[0].get(kwargs.get('attr'))
            click.echo(result)
    else:
        if result:
            click.echo(json.dumps(result[0]))


if __name__ == "__main__":
    cli()