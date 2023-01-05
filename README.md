# Experimento OCR con pytesseract 

## Overview 
1. Este [notebook](https://github.com/pilarcode/notebooks/blob/dev/ocr_recibos_pytesseract.ipynb) contiene un experimento sobre las funcionales que podemos realizar con [Pytesseract](https://pypi.org/project/pytesseract/), una libreria open source para optical character recognition.

2. También contiene un servicio web con [Flask](https://flask.palletsprojects.com/en/2.2.x/) que recibe una imagen codificada en base64 y realiza la extracción de caractéristicas de la imagen del recibo (precio item,descripción item, total). Ese servicio llama a servicios de AWS para la extracción de entidades y utiliza expresiones regulares en el prepocesamiento.

## Notes

- [x]  Explorar un servicio para el reconocimiento de texto en imágenes ( open source) como alternativa al que ya se encuentra disponible en la plataforma de Aws que es de coste.
- [x] Explorar los datasets de facturas o recibos disponibles en el estado del arte para utilizarlo en nuestro caso de uso.
- [x] Tarea de extracción de datos: Dada una imagen de un recibo o ticket de compra obtener el nombre del establecimiento donde se realizo la compra, fecha de la compra y el listado de los productos (establecimiento, nombre producto, precio del producto) en formato texto.
- [ ] Tarea de almacenamiento: Completada la tarea anterior, guardaremos la información del fichero txt en una base de datos NoSQL ( Amazon DynamoDB) para categorizar las compras. Clasificar las compras nos permitirá predecir los gastos que realizará o por ejemplo, sugerirle realizar compras que ya realiza con frecuencia, de forma automática.

<img src="https://github.com/pilarcode/demo-receipt-ocr/blob/main/portada_readme.png" name="ejemplo recibo con las entidades extraidas con Pytesseract" width="400"/>

## Resources
### OCR opensource
- Tesseract https://tesseract-ocr.github.io/ https://opensource.google/projects/tesseract
- Free OCR API https://ocr.space/ocrapi
- Top 5 https://rapidapi.com/blog/top-5-ocr-apis/

###  Datasets
- SROIE2019 https://drive.google.com/drive/folders/1ShItNWXyiY1tFDM5W02bceHuJjyeeJl2
- FUNSD https://guillaumejaume.github.io/FUNSD/
