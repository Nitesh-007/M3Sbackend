from flask import jsonify, Blueprint


designation=Blueprint('designation',__name__)

get_designation=["software engineer","Sr. Software Engineer","Tech Lead", "Sr. Tech Lead"]

@designation.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response


@designation.route('/get_designation',methods=['GET'])

def get_Designation_Data():
    try:
        response={
            "data":get_designation
        }
        return jsonify(response),200
    except Exception as e:
        return jsonify({'message':'error occure','error':str(e)}),500