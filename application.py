from src import *
from flask import Flask, jsonify,request
from src.utilsFile import saveImageBase64,deleteTemporalFiles
from src.receiptFeature import ReceiptFeature


application =  Flask(__name__)


@application.route('/',methods=['GET'])
def main():
	return "Serivice is up",200

@application.route('/extractFeatures',methods=['POST'])
def extractFeatures():
	params = request.get_json()
	image = params['image']
	filename = params['filename']
	saveImageBase64(image,"src/tmp/"+filename)

	receiptFeature = ReceiptFeature()	
	features = receiptFeature.getFeatures(filename)
    
	deleteTemporalFiles(filename)
	return jsonify(features),200


if __name__ == "__main__":
    
	application.run(host="0.0.0.0", port=80, debug = True)