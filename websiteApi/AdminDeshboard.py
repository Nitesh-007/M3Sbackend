
from flask import Blueprint,jsonify,request
from . import mongo

AdminDeshboard=Blueprint('AdminDeshboard',__name__)









task_Data={
   
    "totalTask":32,
    "completedTask":15,
    "incompletedTask":17,
    
    
     "incompletedTaskList":[{
        
        "subjectName":"java",
        "totalAssignmnet":8,
        "submissionDate":"21-jan"
         
       
    },{
        
        "subjectName":"HTML",
        "totalAssignmnet":10,
        "submissionDate":"22-jan"
         
       
    },{
        
        "subjectName":"CSS",
        "totalAssignmnet":14,
        "submissionDate":"24-jan"
         
       
    }],
    "submissionDate":[{
        
            "subjectName":"python",
            "totalAssignmnet":"6",
            "submissionDate":"26-jul"

        }]
}




@AdminDeshboard.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response

@AdminDeshboard.route('/chart',methods=['GET','POST'])
def chart():
    try:
        emploee_collection=mongo.db['Empdata']
       
        result=emploee_collection.find({"employeeType":"MENTOR"})
        mentor_data = list(result)
        
        for mentor in mentor_data:
            mentor['_id'] = str(mentor['_id'])
            mentor.pop('password', None)

        # Count mentors by bussinessUnit
        bussiness_unit_count = {}
        for mentor in mentor_data:
            bussiness_unit = mentor['bussinessUnit']
            if bussiness_unit:
                bussiness_unit_count[bussiness_unit] = bussiness_unit_count.get(bussiness_unit, 0) + 1  
                print("hfhfh",bussiness_unit_count)

        # Construct the chartData JSON
        chart_data = []
        for domain, count in bussiness_unit_count.items():
            chart_data.append({
                "domain": domain,
                "count": count
            })
        

        response =[ {
            #  'data':chartData
            
            "data":chart_data
            # "count":23

        }]

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
    

@AdminDeshboard.route('/mentee',methods=['GET'])    
def get_mentees():
    try:
        emploee_collection=mongo.db['Empdata']
       
        result=emploee_collection.find({"employeeType":"MENTEE"}).limit(4)
        total=emploee_collection.find({"employeeType":"MENTEE"})
        total_mentee=list(total)
        mentee_data = list(result)
        
        for mentee in mentee_data:
            mentee['_id'] = str(mentee['_id'])
            mentee.pop('password', None)
        
        response = {
            'data':mentee_data,
            "message":len(total_mentee)
            }

        return jsonify(response),200
    except Exception as e:
        return jsonify({'message':'An Error occurred', 'error':str(e)}),500
    


@AdminDeshboard.route('/taskdata',methods=['GET'])  
def get_task_data():

    try:
        response={
            'data':task_Data
        }

        return jsonify(response),200
    
    except Exception as e:
        return jsonify({'message':'An Error occured','error':str(e)}),500
    

@AdminDeshboard.route('/profile/<email>',methods=['GET'])
def get_employee_data(email):
    try:
        employee_collection = mongo.db['Empdata']
        
        
        employee = employee_collection.find_one({"email": {"$regex": '^' +email+ '$', "$options": "i"}})
       
        
        if employee:
             employee['_id'] = str(employee['_id'])
             employee.pop('password',None)
             employee.pop('token',None)
             employee.pop('otp',None)
             response={
            'data':employee}
             return jsonify(response), 200     
        else:
            return jsonify({'message': 'Employee not found'}), 404

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
    



@AdminDeshboard.route('/get_employee/<email>',methods=['GET'])
def get_employees(email):
    try:
        employee_collection = mongo.db['Empdata']
        
        
        employee = employee_collection.find_one({"email": {"$regex": '^' +email+ '$', "$options": "i"}})
        if employee:
             employee['_id'] = str(employee['_id'])
             employee.pop('password',None)
             employee.pop('token',None)
             employee.pop('otp',None)
             employee.pop('assignedMentees',None)
             response={
            'data':employee}
             return jsonify(response), 200     
        else:
            return jsonify({'message': 'Employee not found'}), 404

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
    



@AdminDeshboard.route('/update_employee/<email>',methods=['PUT','PATCH'])
def update_employee(email):
    try:
        update_data=request.json
        print("yyyy",update_data)
        employee_collection=mongo.db['Empdata']
        print("hhdhdh",email)
        result=employee_collection.update_one({"email": {"$regex": '^' +email+ '$', "$options": "i"}},{"$set":update_data})
        if result.modified_count > 0:
            return jsonify({'message': 'Employee data updated successfully'}), 200
        else:
            return jsonify({'message': 'No changes made to employee data'}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500    
    

@AdminDeshboard.route('/delete_User/<email>',methods=['DELETE'])   

def delete_user(email):
    try:
        
        employee_collection=mongo.db['Empdata']
        result = employee_collection.delete_one({"email": {"$regex": '^' +email+ '$', "$options": "i"}})

        if result.deleted_count > 0:
            return jsonify({'message': 'User deleted successfully'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500       

        













    




    



    

   





