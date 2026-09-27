from flask import Flask
import os

app = Flask(__name__)

SECRET_API_KEY = os.getenv("SECRET_API_KEY")

@app.route('/')
def hello():
    return "Hello, DevSecOps World!"

if __name__ == '__main__':
    # FIXED: Turned off debug mode and bound to localhost (127.0.0.1) instead of 0.0.0.0
    app.run(host='127.0.0.1', port=8080, debug=False)