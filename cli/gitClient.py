import click
import requests

base_url = "http://localhost:5000"


@click.group()
@click.version_option()
def cli():
    """gitCLI

        Is a simple cli for github
    """

@cli.command('followers')
@click.argument('username', type=str)
def followers(username):
    """Return the number of followers the user have"""
    followers = requests.get(base_url + "/followers/%s" % username).json()
    click.echo('%s have %s followers' % (username, followers))




