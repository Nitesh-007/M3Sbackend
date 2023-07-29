from flask import jsonify,Blueprint

techgroup=Blueprint("techgroup",__name__)

get_tech_group_data=["Angular","react","Wifi",".NEt","5G","android","Ios"]


@techgroup.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response


@techgroup.route("/get_tech",methods=['GET'])
def get_tech_group():
    try:
        response={
            "data":get_tech_group_data
        }
        return jsonify(response),200
    except Exception as e:
        return jsonify({'message':'error occur','error':str(e)}),500
