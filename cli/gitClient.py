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


@cli.command('info') 
@click.argument('username', type=str)
def user_infos(username):
    """Shows some users infos from gith"""

    user = requests.get(base_url + '/user/%s' % username).json()
    click.echo('Info about %s' % user['name'])
    click.echo('')
    click.echo('Bio: "%s"' % user['bio'])
    click.echo('')
    click.echo('- Is from %s' % user['location'])
    click.echo('- Works in %s' % user['company'])
    click.echo('- Have %s public repositories' % user['public_repos'] )
    click.echo('- Is following %s users' % user['following'])
    click.echo('- Have %s followers' % user['followers'] )

