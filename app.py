from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Please this app is useful, myapp, and make payments, TY!!!'
