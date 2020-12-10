#!/usr/bin/python

from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__)

@app.route("/dynconfig")
def config_generator():

    with open("swinfo.json") as f:
        swinfo = json.load(f)

    req_mac = request.headers.get("X-Arista-SystemMAC")
    sw = swinfo.get(req_mac)

    return render_template("config.j2", **sw) if req_mac and sw else ""
