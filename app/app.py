from flask import Flask

app = Flask(__name__)

# Intentionally hardcoded secret for DevSecOps demo purposes
SECRET_API_KEY = "AKIAIOSFODNN7EXAMPLE" 

@app.route('/')
def hello():
    return "Hello, DevSecOps World!"

if __name__ == '__main__':
    # Running in debug mode intentionally for scanning demo
    app.run(host='0.0.0.0', port=8080, debug=True)
