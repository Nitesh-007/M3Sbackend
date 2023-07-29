from flask import jsonify,Blueprint
from . import mongo


allmentee=Blueprint("allmentee",__name__)




@allmentee.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response


@allmentee.route('/mentees',methods=['GET'])

def all_Mentee_Data():
    try:
        emploee_collection=mongo.db['Empdata']
       
        result=emploee_collection.find({"employeeType":"MENTEE"})
        mentee_data = list(result)
        
        for mentee in mentee_data:
            mentee['_id'] = str(mentee['_id'])
            mentee.pop('password', None)
        
        for mentee in mentee_data:
            if 'assignedMentees' not in mentee:
                mentee['assignedMentees'] = 0  
        response={
            "message":len(mentee_data),
            "data":mentee_data
        }
        return jsonify(response),200
    except Exception as e:
        return jsonify({'message':'An error occurred', 'error': str(e)}),500
    


   
