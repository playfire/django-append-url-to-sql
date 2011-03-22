#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-append-url-to-sql',
    description="Appends the request URL to SQL statements in Django.",
    version="0.1",
    url='http://code.playfire.com/django-append-url-to-sql',

    author='Playfire.com',
    author_email='tech@playfire.com',
    license='BSD',

    packages=find_packages(),
)
