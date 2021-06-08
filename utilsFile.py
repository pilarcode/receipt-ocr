import os
import json
import base64

        
def writeFile(output, file):
    with open(file, 'w') as f:
        f.write(output)
    f.close()


def writeFileJson(output, file):
    with open(file, 'w') as f:
        json.dump(output, f)
    f.close()

def readFile(file):
    with open(file) as f:
        lines = [line.rstrip() for line in f]
    f.close()
    return lines

def readFileJson(file):
    with open(file) as f:
        data = json.load(f)
    f.close()
    return data

def readImage(file):
    with open(file, 'rb') as document:
        imageBytes = bytearray(document.read())
    document.close()
    return imageBytes

def deleteImage(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("The file does not exist")

def saveImageBase64(imgstring,path):
	with open(path, 'wb') as f:
		f.write(base64.b64decode(str(imgstring)))
