from flask import Flask

import os
import time

app = Flask(__name__)
threshold = time.time() + 30

@app.route('/')
def root():
    return 'Hello Kubernetes Workshop!'

@app.route('/health')
def health():
    return 'OK'

@app.route('/ready')
def ready():
    if time.time() >= threshold:
        return 'OK'
    else:
        raise Exception('Not ready')

@app.route('/name')
def name():
    return f'Hello from {os.getenv("POD_NAME")}\n'

