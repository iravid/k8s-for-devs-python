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

@app.route('/print-env')
def print_env():
    return f'Env var value: {os.getenv("ENABLE_FEATURE")}\n'

@app.route('/print-envfrom')
def print_envfrom():
    values = [f'{k}: {v}' for (k, v) in os.environ.items() if k.startswith('ENV_FROM_')]
    return f'Env from values: {values}\n'

@app.route('/print-file')
def print_file():
    contents = [line for line in open("/app/config/APPCONF")]
    return f'Data from file: {contents}\n'

