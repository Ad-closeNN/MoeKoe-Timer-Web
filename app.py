"""MoeKoe Timer 网页后端"""
"""
@Created    : 2025/5/2 19:38
@Author     : Ad-closeNN (Ad_closeNN)
@FileName   : app.py
@Software   : PyCharm
@Python     : 3.13.1
"""

import flask
import os
app = flask.Flask(__name__)
@app.route('/')
def index():
    try:
        with open("/tmp/time", "r") as f:
            minute = f.read()
            return flask.render_template("index.html", num=int(minute))
    except FileNotFoundError:
        #minute = "NaN"
        return flask.render_template("error.html")

@app.route("/alive")
def alive():
    """I'm alive!"""
    return flask.Response(status=200)

@app.route("/set")
def setting():
    pwd = flask.request.args.get('pwd')
    minutes = flask.request.args.get("time")
    if minutes and pwd:
        if pwd == os.environ.get('PWD'):
            with open("/tmp/time", "w") as f:
                f.write(minutes)
                return f"time 修改为：{minutes}", 200
        else:
            return flask.Response(status=403)
    else:
        return flask.Response(status=403)

@app.route("/pwd")
def test():
    return os.environ.get('PWD')