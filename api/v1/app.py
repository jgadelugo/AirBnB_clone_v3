#!/usr/bin/python3
"""main app file."""
from flask import Flask, Blueprint

app = Flask(__name__)
from models import storage
from api.v1.views import app_views
app.register_blueprint(app_views, url_prefix="/api/v1")


# declare method to handle @app.teardown_appcontext that calls storage.close()
@app.teardown_appcontext
def teardown(response_or_exc):
    """Close storage when done."""
    storage.close()

host = "0.0.0.0"
port = 5000

if __name__ == "__main__":
    app.run(debug=True, host=host, port=port, threaded=True)
