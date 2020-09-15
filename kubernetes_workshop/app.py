from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello Kubernetes Workshop!'

@app.route('/health')
def health():
    if random.randint(0, 100) <= 50:
        raise Exception("Boom")
    else:
        return 'OK'
