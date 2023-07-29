from flask import jsonify, Blueprint


Bu=Blueprint('Bu',__name__)

BU_Data=["cloud_Mobile","IoT","Networking","Embeded"]


@Bu.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response


@Bu.route('/get_Bu',methods=['GET'])
def get_Bu_Data():
    try:
        response={
            "data":BU_Data
        }
        return jsonify(response),200
    except Exception as e:
        return jsonify({'message':'error occure','error':str(e)}),500