
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Cloud CI/CD Pipeline Using Jenkins</h1>
    <p>My Flask application is running successfully!</p>
    <p>Automatic deployment through GitHub Webhook and Jenkins!</p>
    <p>Deployed using Docker on AWS EC2.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
