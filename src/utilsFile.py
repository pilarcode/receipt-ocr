import os
import json
import base64

        
def writeFile(output, file):
    with open(file, 'w') as f:
        f.write(output)

def writeFileJson(output, file):
    with open(file, 'w') as f:
        json.dump(output, f)

def readFile(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]
    return lines

def readFileJson(file):
    with open(file) as f:
        data = json.load(f)
    return data

def readImage(file):
    with open(file, 'rb') as document:
        imageBytes = bytearray(document.read())
    document.close()
    return imageBytes

def deleteTemporalFiles(image):
    filename, fileExtension = os.path.splitext(image)
    deleteFile("src/tmp/"+image)
    deleteFile("src/text/"+filename+".txt")
    deleteFile("src/tables/"+filename+".txt")
    deleteFile("src/entidades/"+filename+".txt")

def deleteFile(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")

def saveImageBase64(imgstring,path):
	with open(path, 'wb') as f:
		f.write(base64.b64decode(str(imgstring)))
