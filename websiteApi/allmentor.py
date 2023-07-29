from flask import jsonify,Blueprint
from . import mongo
import json

allmentor=Blueprint('allmentor',__name__)






@allmentor.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response


@allmentor.route('/allmentor',methods=['GET'])

def all_Mantoe_Data():
    try:
        emploee_collection=mongo.db['Empdata']
       
        result=emploee_collection.find({"employeeType":"MENTOR"})
        mentor_data = list(result)
        
        for mentor in mentor_data:
            mentor['_id'] = str(mentor['_id'])
            mentor.pop('password', None)
        
        for mentor in mentor_data:
            if 'assignedMentees' not in mentor:
                mentor['assignedMentees'] = 0 
            else:
                mentor['assignedMentees'] = len(mentor['assignedMentees'])       
        
        # for mentor in mentor_data:
        #     mentor_data=len(mentor_data[assignedMentees])
         
        response={
            "data":mentor_data
            
            
        }
        return jsonify(response),200
    except Exception as e:
        return jsonify({'message':'error occure','error':str(e)}),500