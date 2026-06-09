from flask import Flask, jsonify, render_template
import os, datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",
        app_name=os.getenv("APP_NAME", "Assessment Retail/Shine App"),
        version=os.getenv("APP_VERSION", "v1.0"),
        time=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    )

@app.route("/health")
def health():
    return jsonify(status="UP", service="assessment-app")

@app.route("/api/products")
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 55000},
        {"id": 2, "name": "Mobile", "price": 25000},
        {"id": 3, "name": "Headphones", "price": 2000}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)