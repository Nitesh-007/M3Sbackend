from flask import Flask, jsonify, request,Blueprint
import jwt
import random
import string



AdminTaskData=Blueprint('AdminTaskData',__name__)

# A list to store user data (replace with your own user data storage mechanism)
users = [
    {
        "id": "1",
        "mentorName": "nitesh",
        "mentees": "singh",
        "createdTask": '5',
        "completedTask": '3',
        "pendingTask": "2",
        "location": "Noida",
        "totalTask": "8",
        "email": "admin@example.com",
        "password": "Abcd@1234",
        "usertype": "ADMIN"
    },
    {
        "id": "2",
        "mentorName": "niteshsingh",
        "mentees": "ranasingh",
        "createdTask": '8',
        "completedTask": '3',
        "pendingTask": "5",
        "location": "pune",
        "totalTask": "8",
        "email": "mentor@example.com",
        "password": "Abcd@1234",
        "usertype": "MENTOR"
    },
    {
        "id": "3",
        "mentorName": "niteshsinghrajpoot",
        "mentees": "ranasinghrajpoot",
        "createdTask": '8',
        "completedTask": '3',
        "pendingTask": "5",
        "location": "bgs",
        "totalTask": "8",
        "email": "mentee@example.com",
        "password": "Abcd@1234",
        "usertype": "MENTEE"
    }
]



# Secret key for JWT token encoding/decoding (replace with your own secret key)
# app.config['SECRET_KEY'] = 'your-secret-key'


# Enable CORS (Cross-Origin Resource Sharing)
@AdminTaskData.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response


# Task route
@AdminTaskData.route('/task', methods=['GET'])
def task():
    try:
        response = {
            'data': users
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500