from flask import jsonify,Blueprint
from . import mongo


location=Blueprint('location',__name__)


All_location=["Noida","GuruGram","mathura","patna","Begusarai","Darbhnaga","Ranchi"]





@location.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response



@location.route('/get_location',methods=['GET'])

def location_Data():

    try:

        # locationData=mongo.db['Empdata']
        # result=locationData.find_one({'All_location':["Noida","GuruGram","mathura","patna","Begusarai","Darbhnaga","Ranchi"]})
        # for result in result:
        #     result['_id']=str(result['_id'])
        # print(result)
        


        response={"data":All_location}
        return jsonify(response),200
    except Exception as e:
        return jsonify({'message':'error occure','error':str(e)}),500
        