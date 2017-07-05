#!/usr/bin/python2

from wsgiref.handlers import CGIHandler

from urlcf.wsgi import app

if __name__ == "__main__":
    CGIHandler().run(app)
