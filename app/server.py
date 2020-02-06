# coding: utf-8
import os
import json
import RPi.GPIO as GPIO
from datetime import datetime
from flask_cors import CORS
from flasgger import Swagger
from flask import Flask, jsonify, request

server = Flask(__name__)
CORS(server)

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

def pin_down(LED):
    GPIO.setup(LED, GPIO.OUT) #Active le contrôle du GPIO
    GPIO.output(LED, GPIO.LOW) #On l’éteint

def pin_up(LED):
    GPIO.setup(LED, GPIO.OUT) #Active le contrôle du GPIO
    GPIO.output(LED, GPIO.LOW) #On l’éteint

@server.route('/api/move/right/start', methods=["GET"])
def run():
    try:
        pin_up(40)
        return jsonify("OK")
    except Exception as e:
        return jsonify(e)
@server.route('/api/move/right/stop', methods=["GET"])
def run():
    try:
        pin_down(40)
        return jsonify("OK")
    except Exception as e:
        return jsonify(e)

@server.route('/api/move/left/start', methods=["GET"])
def run():
    try:
        pin_up(41)
        return jsonify("OK")
    except Exception as e:
        return jsonify(e)

@server.route('/api/move/left/stop', methods=["GET"])
def run():
    try:
        pin_down(41)
        return jsonify("OK")
    except Exception as e:
        return jsonify(e)

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


def init():
    printf("Starting... iRobot")
    GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
    GPIO.setwarnings(False) #On désactive les messages d'alerte
    printf("Started iRobot")

# note you can pass in multiple rows for scoring

if __name__ == '__main__':
    init()
    server.run(host="0.0.0.0", port=80)

