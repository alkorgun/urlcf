"""
Created on Jul 5, 2017

@author: alkorgun
"""

import os
import sys

from .wsgi import app


class UrlcfService(object):

    pid_file = "/tmp/urlsf-service.pid"

    default_pipe = "/dev/null"
    default_folder = "/tmp"

    def daemonize(self): # by Sander Marechal
        """
        UNIX double-fork magic.
        """
        pid = os.fork()
        if pid:
            sys.exit(2)

        os.setsid()
        os.chdir(self.default_folder)
        os.umask(0)

        pid = os.fork()
        if pid:
            sys.exit(2)

        sys.stdout.flush()
        sys.stderr.flush()

        si = open(self.default_pipe, "r")
        so = open(self.default_pipe, "a+")
        se = open(self.default_pipe, "a+", 0)

        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        with open(self.pid_file, "w") as fp:
            fp.write(str(os.getpid()))

    def start(self):
        self.daemonize()
        self.run()

    def run(self):
        app.run(
            host="0.0.0.0",
            port=80
        )
