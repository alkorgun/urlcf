"""
@author: alkorgun
"""

import os

from distutils.core import setup
from distutils.command.install import install

import urlcf.db

name = "urlcf"
version = os.getenv("version") or "1.0.0"


class Initializer(install):

    def run(self):
        install.run(self)
        urlcf.db.init()


def ls(folder):
    files = []
    for name in os.listdir(folder):
        filename = os.path.join(folder, name)
        if os.path.isdir(filename):
            files.extend(ls(filename))
            continue
        files.append(filename)
    return files


files = {
    "/etc/init.d": ["init.d/urlcf"],
    "/usr/bin": ["scripts/urlcf-run8080"],
    "/usr/lib/cgi-bin": ["scripts/urlcf.cgi"],
    "/var/lib/urlcf/html": ls("html")
}


if __name__ == "__main__":
    setup(
        name=name,
        version=version,
        author="alkorgun",
        author_email="alkorgun@gmail.com",
        description="",

        packages=["urlcf"],

        requires=[
            "flask",
            "sqlalchemy"
        ],

        data_files=files.items(),

        cmdclass={
            "install": Initializer
        }
    )
