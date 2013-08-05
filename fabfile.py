# -*- coding: utf-8 -*-

# http://docs.fabfile.org/en/1.5/tutorial.html

from fabric.api import *

project = "fbone"

# the user to use for the remote commands
env.user = ''
# the servers where the commands are executed
env.hosts = ['']


def apt_get(*packages):
    sudo('apt-get -y --no-upgrade install %s' % ' '.join(packages), shell=False)

def setup():
    """
    Setup virtual env.
    """

    apt_get("python-pip libmysqlclient-dev python-dev postgresql-9.1")
    local("apt-get -y build-dep python-psycopg2")
    local("virtualenv env")
    activate_this = "env/bin/activate_this.py"
    execfile(activate_this, dict(__file__=activate_this))
    local("python setup.py install")
    reset()

def create_database():
    """Creates role and database"""
    db_user = 'ss' # define these
    db_pass = 'ss'
    db_table = 'CrossPollinationProj'
    sudo('psql -c "CREATE USER %s WITH NOCREATEDB NOCREATEUSER ENCRYPTED PASSWORD E\'%s\'"' % (db_user, db_pass), user='postgres')
    sudo('psql -c "CREATE DATABASE %s WITH OWNER %s"' % (
        db_table, db_user), user='postgres')





