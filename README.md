# GitCLI

Its a simple cli to get some informations about users of github, this project is made just for learning proposal (**Click**  and **Flask**)

## Installation configs

First, its necessary install the pipenv

```bash
sudo apt-get install pipenv
```
So then, **clone the repository** and execute this commands

``` bash

# Install api dependecies
$ cd banckend && pipenv install

# enter the backend virtualenv
$ pipenv shell

# run the API
$ python3 server.js

# install cli dependencies
$ cd cli/ && pipenv install 

# enter the cli virtualenv
$ pipenv shell

# Create an virtualenv using the setup.py
$ pip install --editable .

# Use the gitcli
$ gitcli [OPTIONS] COMMAND [ARGS]

# exit the virtualenv
$ deactivate
```

Obs: This project in running in Python3
