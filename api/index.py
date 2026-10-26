import os
import sys

# Ensure the project root directory is in sys.path for module resolution
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Import the Flask application instance
from app import app

# Safety alias: In case Vercel rewrites directly to /api/index
if "vercel_index" not in app.view_functions:
    @app.route("/api/index", methods=["GET"])
    def vercel_index():
        return app.view_functions["index"]()
