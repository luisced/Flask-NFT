from email import message
from flask import Blueprint, request, jsonify, make_response

users = Blueprint('users', __name__)


@users.route('/users', methods=['GET'])
def index():
    message = {
        'message': 'Initialize App Successfully'
    }
    return jsonify(message), 200
