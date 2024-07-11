import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Flask, request, jsonify, make_response
from flask_restx import Resource, Api
from flask_cors import CORS
from recommend import recommend
import json



app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
api = Api(app)




# @api.route('/sentence/insert')
# class Sentence(Resource):
#     def post(self):
#         gender = request.json.get('gender')
#         input_text = request.json.get('input_text')
#         input_image = '../Wav2Lip/my_data/'+request.json.get('character')
#         out_path = request.json.get('out_path')
#         filename = request.json.get('filename')
#         return jsonify({'success': generate_lipsync.generate(gender,input_text,input_image,out_path,filename),'path':out_path+filename});

@api.route('/challenge/recommend')
class Challenge(Resource):
    def post(self):
        data = request.json
        print(data)
        return recommend(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 35281)))