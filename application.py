from flask import Flask, jsonify,request
from utilsFile import *
from receiptFeature import *

app = Flask(__name__,static_folder='tmp')

@app.route('/extractFeatures',methods=['POST'])
def base64upload():
	#Modelo de entrada del servicio rest
	params = request.get_json()
	image = params['image']
	filename = params['filename']
	path = "tmp/"+filename

	#Guardar imagen directorio temporal
	saveImageBase64(image,path)

	#Extraer las features
	extractor = ReceiptFeature()	
	features = extractor.processTmpFile("tmp",filename)
    
	#Borrar la imagen del directorio temporal
	#deleteImage(path)	
	return jsonify(features),200



if __name__ == "__main__":
    app.run(debug=True)