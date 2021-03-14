from flask import Blueprint, jsonify

MAIN_ROUTE = Blueprint('main', __name__)


@MAIN_ROUTE.route("/", methods=["GET"])
def index():
    return jsonify(message="Hello There world"), 200