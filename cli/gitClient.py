import click
import requests
import json

base_url = "http://localhost:5000"


@click.group()
@click.version_option()
def cli():
    """gitCLI

        Is a simple cli for github
    """
    pass

@cli.command('followers')
@click.argument('username', type=str)
def followers(username):
    """Return the number of followers the user have"""
    followers = requests.get(base_url + "/followers/%s" % username).json()
    click.echo('%s have %s followers' % (username, followers))


def write_to_json_file(path, file_name, data):
    file_path = './' + path + '/' + file_name + '.json' 
    with open(file_path, 'w') as fp:
        json.dump(data, fp)

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

    path = '../infos'
    file_name = "%s" % user['login']
    write_to_json_file(path, file_name, user) 


@cli.command('following')
@click.argument('user1', type=str, required=True)
@click.argument('user2', type=str, required=True)
def checking_follow(user1, user2):
    """Checks and returns if a user is following other"""

    is_following = requests.get(base_url+'/user/%s/following/%s' % (user1, user2)).json()

    if(is_following == 204):
        click.echo('%s is following %s' % (user1, user2))
    
    elif(is_following == 404):
        click.echo('%s is not following %s' % (user1, user2))

if __name__ ==  "__main__":
    cli()
