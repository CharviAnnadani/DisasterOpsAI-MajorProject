from flask import Flask
from routes.sos_routes import sos_bp

app = Flask(__name__)

app.register_blueprint(sos_bp)

@app.route("/")
def home():
    return {
        "project": "DisasterOps AI",
        "status": "Running",
        "available_routes": [
            "/sos"
        ]
    }

if __name__ == "__main__":
    app.run(debug=True)