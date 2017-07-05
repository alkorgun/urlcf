#!/bin/bash

# tox -e py27
python setup.py --command-packages=stdeb.command bdist_deb
