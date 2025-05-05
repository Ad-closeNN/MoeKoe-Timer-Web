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
import datetime
app = flask.Flask(__name__)
@app.route('/')
def index():
    try:
        with open("/tmp/time", "r") as f:
            minute = f.read()
        hours = int(minute) // 60
        remaining_minutes = int(minute) % 60
        with open("/tmp/change_time", "r", encoding="utf-8") as f:
            ct = f.read()
        return flask.render_template("index.html", h=f"{hours}", m=f"{remaining_minutes}", ctime=f"{ct}")
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
        if pwd == os.environ.get('password'):
            with open("/tmp/time", "w") as f:
                f.write(minutes)
            change_time = datetime.datetime.now(datetime.timezone.utc).astimezone(datetime.timezone(datetime.timedelta(hours=8))).strftime("%Y/%m/%d %H:%M:%S")
            with open("/tmp/change_time", "w", encoding="utf-8") as f:
                f.write(change_time)
            return flask.render_template("time.html", m=f"{minutes}", ctime=f"{change_time}"), 200
        else:
            return flask.Response(status=403)
    else:
        return flask.Response(status=403)

"""A PASSWORD TEST"""
"""
@app.route("/pwd")
def test():
    return os.environ.get('password')
"""