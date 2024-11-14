from flask import jsonify, Flask, request
from flask_cors import CORS
from feature_extraction.disease_feature import DiseaseFeature
from feature_extraction.bert_feature import BertFeature
import json
import pickle
import numpy as np

# file = open("model/model_ovr.pkl",'rb')
# model = pickle.load(file)
# file.close()


app = Flask(__name__)
CORS(app)


@app.route('/')
def index() :
    return 'hello world'
 
@app.route('/api/disease-check', methods=['POST'])
def check_disease() :
    '''
{
    "demam" : 1,
    "batuk" : 0,
    "lemes" : 1,
    "sesak nafas" : 0, 
    "age" : 40,
    "gender" : 1,
    "tekanan" : 2,
    "kolesterol" : 0

    "symtoms":
    
}
    '''
    data = request.get_json()
    # symtoms = data['symtoms']
    feature = DiseaseFeature(data)
    res = {
        'result' : data['symtoms'],
        'Message' : "kamu ganteng"
    }
    return jsonify(res), 200 

@app.route('/api/bert', methods= ['POST'])
def bert() :
    '''
        data = {
            "sentence" : "bla bla bla"
        }
    '''
    data = request.get_json()
    bert = BertFeature(data['sentence'])
    topics = bert.get_key_topics()
    filtered_data = {k: v for k, v in topics.items() if v > 0.5}
    res = {
        'result' : filtered_data,
    }


    return jsonify(res), 200 

if __name__ == "__main__" :
    app.run(debug=True, port=8080)