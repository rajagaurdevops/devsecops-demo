from flask import Flask
import os

app = Flask(__name__)

SECRET_API_KEY = os.getenv("SECRET_API_KEY")

@app.route('/')
def hello():
    return "Hello, DevSecOps World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)