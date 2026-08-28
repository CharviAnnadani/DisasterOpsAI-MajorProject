from flask import Flask
from flask_cors import CORS

from routes.sos_routes import sos_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(sos_bp)

@app.route("/")
def home():
    return {
        "project": "DisasterOps AI",
        "status": "Running",
        "available_routes": ["/sos"]
    }

if __name__ == "__main__":
    app.run(debug=True)