# -*- coding: utf-8 -*-

from flask.ext.script import Manager


from reddit_parser import db,Article,Comment,create_app,get_reddits,get_reddits_of_user



app = create_app()
manager = Manager(app)



@manager.command
def run():
    """Run in local machine."""

    app.run(host='0.0.0.0')


@manager.command
def initdb():
    """Init/reset database."""

    db.drop_all()
    db.create_all()

@manager.command
def run_parser():
  get_reddits()
  get_reddits_of_user()

manager.add_option('-c', '--config',
                   dest="config",
                   required=False,
                   help="config file")

if __name__ == "__main__":
    manager.run()
