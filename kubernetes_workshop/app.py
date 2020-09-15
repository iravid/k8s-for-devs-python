from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello Kubernetes Workshop!'

@app.route('/health')
def health():
    return 'OK'
