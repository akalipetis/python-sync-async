import random
import time

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'hello': 'world'})

@app.route('/wait')
def wait():
    wait_millis = random.randint(10, 30)
    time.sleep(wait_millis / 1000.0)
    return jsonify({'wait': wait_millis})

@app.route('/blocked')
def blocked():
    rounds = random.randint(10000, 100000)
    for _ in range(rounds):
        pass
    return jsonify({'rounds': rounds})
