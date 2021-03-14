from flask import Flask, jsonify


def create_app():

    try:

        app = Flask(__name__)

        from .routes import MAIN_ROUTE
        app.register_blueprint(MAIN_ROUTE, url_prefix = '/api')

        return app

    except Exception as e:
        print("Error creating the application %s"%(e))