import src
from flask import Flask, jsonify,request
from src.utilsFile import saveImageBase64,deleteTemporalFiles
from src.receiptFeature import ReceiptFeature

app = Flask(__name__)

@app.route('/',methods=['GET'])
def main():
	message ="Service is UP!"
	return jsonify(message),200


@app.route('/extractFeatures',methods=['POST'])
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
    app.run(debug=True)