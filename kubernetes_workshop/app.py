from flask import Flask

import os

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello Kubernetes Workshop!'

@app.route('/health')
def health():
    return 'OK'

@app.route('/ready')
def ready():
    return 'OK'

@app.route('/name')
def name():
    return f'Hello from {os.getenv("POD_NAME")}\n'

