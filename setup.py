# -*- coding: utf-8 -*-

from setuptools import setup

project = "reddit_parser"

setup(
    name=project,
    version='0.1',
    url='https://github.com/ahsanali/reddit',
    description='CrossPollinationProj is sub reddit parser to visualize sub redits in a different way',
    author='Ahsan Ali',
    author_email='sn.ahsanali@gmail.com',
    packages=["reddit_parser"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-WTF',
        'Flask-Script',
        'Flask-Babel',
        'Flask-Testing',
        'Flask-Mail',
        'Flask-Cache',
        'Flask-Login',
        'Flask-OpenID',
        'nose',
        'mysql-python',
        'tornado',
        'psycopg2'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)
