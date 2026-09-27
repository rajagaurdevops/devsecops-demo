from flask import Flask

app = Flask(__name__)

# Fake Slack Bot Token (Trufflehog catches this easily)
SLACK_BOT_TOKEN = "xoxb-123456789012-1234567890123-abcdef1234567890abcdef12"

@app.route('/')
def hello():
    return "Hello, DevSecOps World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
