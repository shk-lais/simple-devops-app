from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from DevOps CI/CD Pipeline!"

@app.route("/metrics")
def metrics():
    # simple Prometheus-style metric for demo
    return "app_requests_total 1\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

