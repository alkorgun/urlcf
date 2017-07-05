# coding: utf-8

"""
Created on Jul 5, 2017

@author: alkorgun
"""

import traceback

from flask import Flask, render_template, request, redirect, jsonify

from . import db
from .exceptions import *

app = Flask(__name__)
app.template_folder = "/var/lib/urlcf/html"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<uid>", methods=["GET"])
def get(uid):
    try:
        url = db.get(uid)
    except LookupError:
        return render_template("nourl.html")
    return redirect(url, 303)


@app.route("/put", methods=["PUT"])
def put():
    url = request.args["url"]
    uid = db.put(url)
    return jsonify(dict(
        url=url,
        uid=uid
    )), 200


@app.errorhandler(UIDNotFoundError)
def err_204(e):
    """
    Requeted UID is not present in the database.
    """
    return jsonify(dict(
        errno=0,
        alert="Not found."
    )), 204


@app.errorhandler(400)
def err_400(e):
    """
    Query arguments error.
    """
    return jsonify(dict(
        errno=0,
        alert="Input error."
    )), 400


@app.errorhandler(Exception)
def err_500(error):
    """
    Uncatched exceptions handler.
    """
    efmt = traceback.format_exc()
    # app.logger.error(efmt)
    # app.logger.debug(vars(request))
    return jsonify(dict(
        alert="Server error.",
        data=efmt
    )), 500
