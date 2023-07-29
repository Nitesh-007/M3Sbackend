from flask import jsonify, Blueprint, request
from . import mongo  # Import the 'mongo' object
from secrets import choice

import string
import random
import base64

Empdata = Blueprint("Empdata", __name__)

# ...
def generate_password():
    length = 8  # Length of the generated password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one capital letter, one lowercase letter, one digit, and one special character
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

@Empdata.route('/employees', methods=['POST'])



def add_employee():
    try:
        employee_data = request.json

        # Check if user already exists with the same email ID
        employees_collection = mongo.db['Empdata']
        existing_user = employees_collection.find_one({"email": employee_data["email"]})
        print("user data",existing_user)
        if existing_user:
            response = {'message': 'User already exists with the same email ID'}
            return jsonify(response), 409
       
        auto_generated_password = generate_password()
        print(auto_generated_password)
        encoded_password = base64.b64encode(auto_generated_password.encode('utf-8')).decode('utf-8')
        employee_data["password"] = encoded_password
        employee_data["otp"] = ""
        employee_data["token"] = ""
        if employee_data.get('employeeType')=="MENTOR":
            employee_data["assignedMentees"] = []

        if employee_data.get('employeeType')=="MENTEE":
            employee_data["MentorName"] =""    
       
       


        


        
        result = employees_collection.insert_one(employee_data)

        
        

        response = {
            'message': 'Employee added successfully',
            'employee_id': str(result.inserted_id)
        }
        return jsonify(response), 201
    except Exception as e:
        return jsonify({'message': 'Error occurred', 'error': str(e)}), 500
