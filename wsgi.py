"""
WSGI entry point for production deployment
"""

import os
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from main import app
    application = app
    logging.info("WSGI application loaded successfully")
except Exception as e:
    logging.error(f"Error loading WSGI application: {e}")
    from flask import Flask, jsonify
    application = Flask(__name__)
    
    @application.route('/')
    def index():
        return jsonify({"status": "error", "message": f"Failed to load main application: {str(e)}"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port)
