#!/usr/bin/env python3
# coding: utf-8
import os
import json
from datetime import datetime
from flask_cors import CORS
from flasgger import Swagger
from flask import Flask, jsonify, request
from flask import send_from_directory
from gpiozero import LED

server = Flask(__name__)
CORS(server)
script_path=os.path.dirname(__file__)

server.config['SWAGGER'] = {
    "swagger_version": "2.0",
    "title": "iRobot",
    "specs": [
        {
            "version": "1.0.0",
            "title": "iRobot",
            "endpoint": 'spec',
            "route": '/api/spec',
            "rule_filter": lambda rule: True  # all in
        }
    ],
    "static_url_path": "/api/apidocs"
}

Swagger(server)


@server.route('/api/move/right/start', methods=["GET"])
def start_right():
    try:
        LED(40).on()
        return jsonify("OK")
    except Exception as e:
        return jsonify(e)
@server.route('/api/move/right/stop', methods=["GET"])
def stop_right():
    try:
        LED(40).off()
        return jsonify("OK")
    except Exception as e:
        return jsonify(e)

@server.route('/api/move/left/start', methods=["GET"])
def start_left():
    try:
        LED(38).on()
        return jsonify("OK")
    except Exception as e:
        return jsonify(e)

@server.route('/api/move/left/stop', methods=["GET"])
def stop_left():
    try:
        LED(38).off()
        return jsonify("OK")
    except Exception as e:
        return jsonify(e)

@server.route('/', defaults={'path': 'index.html'})
@server.route('/<path:path>')
def send_static(path):
    
    if(os.path.exists(os.path.join(script_path, 'static/'+path))):
        return send_from_directory('static', path)
    else:
        print("File not found :"+path)
        return send_from_directory('static', 'index.html') 


def init():
    print("Starting... iRobot")

if __name__ == '__main__':
    init()
    server.run(host="0.0.0.0", port=3001)

