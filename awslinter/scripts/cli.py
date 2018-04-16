# Skeleton of a CLI

import click

import awslinter


@click.command('awslinter')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(awslinter.has_legs)
