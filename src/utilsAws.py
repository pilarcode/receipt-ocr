import boto3
from src.utilsFile import readImage
from src.trplib import Document
from src.utilsPrice import formatPrice,isPrice

# Explicit Client Configuration
#session = boto3.Session(profile_name='pilar_dev')

def detectDocumentText(imageFile):
    imageBytes = readImage(imageFile)

    # Amazon Textract client
    textract = boto3.client('textract',region_name = 'us-east-1')

    # Call Amazon Textract
    response = textract.detect_document_text(Document={'Bytes': imageBytes})

    text=""
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            text+= item["Text"]+"\n"
    return text

def detectEntitiesFromText(text):
    # Amazon Comprehend client
    comprehend = boto3.client('comprehend',region_name = 'us-east-1')

     # Call Amazon Textract
    response =  comprehend.detect_entities(LanguageCode="en", Text=text)

    entities = {}
    for entity in response["Entities"]:
        key = entity["Type"]
        value = entity["Text"]
        if key in entities:
            lista = entities[key]
            lista.append(value)
            entities[key] = lista
        else:
            entities[key] = [value]   
    return entities  

def detectDocumentTable(imageFile):
    imageBytes = readImage(imageFile)

    # Amazon Textract client
    textract = boto3.client('textract',region_name = 'us-east-1')

    # Call Amazon Textract
    response = textract.analyze_document(Document={'Bytes': imageBytes},FeatureTypes=['TABLES'])

    #Extract Products
    items = {}
    doc = Document(response)
    for page in doc.pages:
        for table in page.tables:
            for r, row in enumerate(table.rows):
                product  = ""
                price = 0
                for c, cell in enumerate(row.cells):
                    if (isPrice(cell.text)):
                        price = formatPrice(cell.text)
                    else:
                        product += cell.text 
                items[product] = price
        
    return items    
