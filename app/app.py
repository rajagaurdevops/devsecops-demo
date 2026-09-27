from flask import Flask

app = Flask(__name__)

# Let's use a random-looking key instead of the AWS official example key
SECRET_API_KEY = "AKIA1234567890ABCDEF" 

@app.route('/')
def hello():
    return "Hello, DevSecOps World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
