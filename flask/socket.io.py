# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 00:36:24 2016

@author: yl
"""

is_pi = 0

if is_pi:
    import random
    import max7219.led as led
    import time
    from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT

    rc = lambda x: int(x * random.random())
    device = led.matrix(cascaded=1)
    device.orientation(180)
    device.brightness(15)

    def flush_device(buf):

        w = len(buf[0])
        h = len(buf)
        device.clear()
        for y in range(h):
            for x in range(w):
                if buf[x][y] != 0:
                    device.pixel(x, y, 1)

    def code_buffer(code):
        device._buffer = code
        device.flush()


else:
    import webbrowser


from flask import Flask, abort, render_template, redirect, url_for, g
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.debug = False

socketio = SocketIO(app)

import os

print(os.path.abspath("."))
path = r"C:/Users/yl/Desktop/py/python/raspberry/RetroPython/"
path = "../"
if is_pi == 1:
    path = "./"


players = [0, 0]


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Url wrong! 404 not found</h1>", 404


@app.errorhandler(403)
def page_not_found(e):
    return "<h1>Already has two plyer,please wite for a while Ture</h1>", 403


@socketio.on("disconnect", namespace="/game")
def test_disconnect():
    print("Client disconnected")


@app.route("/canvas")
def show_canvas():
    h = "RetroPython.html"
    f = open(path + h)
    html = f.read()
    f.close()
    return html


@app.route("/0")
def get_0_page():

    return redirect("/canvas")


@app.route("/")
def get_index_page():

    return redirect("/2")


@app.route("/static/<filee>")
def get_static(filee):
    f = open(path + "static/" + filee)
    html = f.read()
    f.close()

    return html


@app.route("/2")
def get_p2():

    f = open(path + "p2.html")
    html = f.read()
    f.close()
    return html


@app.route("/1")
def get_p1():

    f = open(path + "p1.html")
    html = f.read()
    f.close()
    return html


@socketio.on("testLine", namespace="/game")
def test_connect(message):
    print(message["data"])
    emit("testLine", {"data": "successed to phone!", "count": 0})


@socketio.on("p2_to_p1", namespace="/game")
def p2_to_p1(p2):
    emit("p2_to_p1", p2, broadcast=True)


@socketio.on("p1_to_pc", namespace="/game")
def p2_to_p1(p1):
    emit("p1_to_pc", p1, broadcast=True)


@socketio.on("end", namespace="/game")
def end(result):  # game over
    emit("end", result, broadcast=True)

    message = "p" + str(result) + " win! "
    if is_pi == 0:
        return
    if result == 0:
        message == "Die together!,no winer! "
    for i in range(2):
        device.show_message(message, font=SINCLAIR_FONT)


@socketio.on("buffer", namespace="/game")
def led_buffer(buff):
    code_buffer(buff)


if __name__ == "__main__":

    socketio.run(app, host="0.0.0.0", port=80)
