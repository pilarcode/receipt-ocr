# Experimento OCR con pytesseract 

1. Este [notebook](https://github.com/pilarcode/notebooks/blob/dev/ocr_recibos_pytesseract.ipynb) contiene un experimento sobre las funcionales que podemos realizar con [Pytesseract](https://pypi.org/project/pytesseract/), una libreria open source para optical character recognition.

2. También contiene un servicio web con [Flask](https://flask.palletsprojects.com/en/2.2.x/) que recibe una imagen codificada en base64 y realiza la extracción de caractéristicas de la imagen del recibo (precio item,descripción item, total). Ese servicio llama a servicios de AWS para la extracción de entidades y utiliza expresiones regulares en el prepocesamiento.



<img src="https://github.com/pilarcode/demo-receipt-ocr/blob/main/portada_readme.png" width=200 name="ejemplo recibo con las entidades extraidas con Pytesseract" class="center" style=".center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}"/>
