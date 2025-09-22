from flask import jsonify, request,Blueprint,current_app
from flask_cors import CORS
import base64
import secrets

import jwt
import random
import string
from . import mongo
import bcrypt

Auth=Blueprint('Auth',__name__)
CORS(Auth)



   


 



# Enable CORS (Cross-Origin Resource Sharing)
@Auth.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response


# Login route
@Auth.route('/user/login', methods=['POST'])
def login():
    try:
        
        email = request.json.get('email')
        print("Email",email)
        password = request.json.get('password')
        print("password",password)

        # Check if email and password are provided
        if not email or not password:
            return jsonify({'message': 'Email and password are required'}), 400

        # Check if user exists and password is correct
        employees_collection=mongo.db['Empdata']
        print(employees_collection)
        
        user = employees_collection.find_one({"email": {"$regex": '^' + email + '$', "$options": "i"}})
        print("user data",user)
        
        # user = next((user for user in users.values() if user['email'] == email), None)
        # print("user data",user)
        if not user:
            return jsonify({'message': 'Invalid email '}), 402

        if  user['password'] != password:
            
            return jsonify({'message': 'Invalid  password'}), 402
        
        
       

        # Generate JWT token
        
        token = generate_token(user)
        employees_collection.update_one({"email": email}, {"$set": {"token": token}})
        # Prepare response
        response = {
            'message': 'Login successful',
            'token': token,
            'email': user['email'],
            'employeeType': user['employeeType'],
            'employeeName': user['employeeName']
        }

        return jsonify(response), 200

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500


# Helper function to generate JWT token
def generate_token(user):
    token_length = 50  # Length of the generated token
    characters = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(characters) for _ in range(token_length))
    return token


#Forgot route
CORS(Auth, support_credentials=True)
@Auth.route('/user/sendEmail', methods=['POST'])
def forgot():
    try:
        user_email=request.json.get('email')
        employees_collection = mongo.db['Empdata']
        user = employees_collection.find_one({"email": {"$regex": '^' + user_email + '$', "$options": "i"}})

        if user:
            otp = generate_otp()
            employees_collection.update_one({"email": user_email}, {"$set": {"otp": otp}})
            response = {'email':user_email,
                        'code':0}
            return jsonify(response),200
        else:
            response={'message':'User not exists please enter a valid email',
                      'code':-1}
            return jsonify(response),409

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
def generate_otp():
    otp_length = 4  # Length of the OTP
    otp_characters = string.digits  # Only use digits for the OTP

    otp = ''.join(random.choice(otp_characters) for _ in range(otp_length))
    return otp    
    

@Auth.route('/user/changePassword', methods=['POST'])    
def change_password():
    try:
        request_data = request.json

        email = request_data['email']
        old_password = request_data['oldPassword']
        new_password = request_data['newPassword']
        confirm_password = request_data['confirmPassword']


         # Check if the new password and confirm password match
        if new_password != confirm_password:
            response = {'message': 'New password and confirm password do not match'}
            return jsonify(response), 400
        
        employees_collection = mongo.db['Empdata']
        user = employees_collection.find_one({"email": {"$regex": '^' + email + '$', "$options": "i"}})

        stored_password = user["password"]
        if stored_password != old_password:
            response = {'message': 'Invalid old password'}
            return jsonify(response), 400
        

        # Encode the new password and update it in the database
        # encoded_new_password = base64.b64encode(new_password.encode('utf-8')).decode('utf-8')
        result = employees_collection.update_one({"email": email}, {"$set": {"password":new_password}})

        if result.modified_count > 0:
            response = {'message': 'Password changed successfully',
                        'code':0}
            return jsonify(response), 200
        else:
            response = {'message': 'No changes made to the password'}
            return jsonify(response), 200

        
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
    

@Auth.route('/user/validateOtp',methods=['POST'])  
def get_otp():
    try:
        email=request.json.get('email')
        otp=request.json.get('otp')

        employees_collection = mongo.db['Empdata']
        user = employees_collection.find_one({"email": {"$regex": '^' + email + '$', "$options": "i"}})
      

        if user['otp'] == otp:
            response = {
                "message": "OTP matched",
                "code": 0
            }
            return jsonify(response), 200
        else:
            response = {
                "message": "OTP did not match",
                "code": -1
            }
            return jsonify(response), 409
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500  



@Auth.route('/user/reset', methods=['POST'])   
def reset_password():
    try:
        request_data = request.json

        email = request_data['email']
        new_password = request_data['newPassword']
        confirm_password = request_data['confirmPassword']


         # Check if the new password and confirm password match
        if new_password != confirm_password:
            response = {'message': 'New password and confirm password do not match'}
            return jsonify(response), 400
        
        employees_collection = mongo.db['Empdata']
        result = employees_collection.update_one({"email": email}, {"$set": {"password":new_password}})
        if result.modified_count > 0:
            response = {'message': 'Password changed successfully',
                        'code':0}
            return jsonify(response), 200
        else:
            response = {'message': 'No changes made to the password'}
            return jsonify(response), 200    
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500









    
   
        
        
