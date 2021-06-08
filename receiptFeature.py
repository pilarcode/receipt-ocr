#from platform import processor
import utilsAws as aws
from utilsFile import *
from dateFeature import *
from productFeature import *
from shopFeature import *
import os

class ReceiptFeature:

  def __init__(self):
    self.textDirectory = 'text'
    self.entitiesDirectory = 'entidades'
    self.tablesDirectory ='tables'
  
  
  def processTmpFile(self,dir, file):
    self.tmpDirectory = dir

    print("Procesando el fichero: {}".format(file))
    # Obtiene el texto de la imagen con aws
    #text = self.saveTextDetectedByTextract(dir,file)
    # Obtiene las entidades con aws"
    #entities=self.saveEntitiesDetectedByComprehed(self.entitiesDirectory,file,text)
    # Obtiene la relaciones tabulares de la imagen con aws
    #table = self.saveTableDetectedByTextract(dir,file)
    # Extrae la features
    features = {}
    text = self.readText(file)
    table = self.readTable(file)
    entities = self.readEntities(file)  
    
    extractor = ShopFeature(entities,text)
    features['shop'] = extractor.process()
    extractor = DateFeature(entities)
    features['date']  = extractor.process()
    extractor = ProductFeature(table,text)
    features['items'] = extractor.process()
    return features

  def saveTextDetectedByTextract(self,dir,file):    
    inputfile = dir + "/" + file
    text = aws.detectDocumentText(inputfile)
    filename, fileExtension = os.path.splitext(file)
    outputfile = self.textDirectory + "/"+ filename + ".txt"  
    writeFile(text,outputfile)
    return text
      
  def saveEntitiesDetectedByComprehed(self,dir,file,text):
    entities = aws.detectEntitiesFromText(text)
    filename, fileExtension = os.path.splitext(file)
    outputfile = dir + "/"+ filename + ".txt"  
    writeFileJson(entities,outputfile)
    return entities
  
  def saveTableDetectedByTextract(self, dir, file):
    inputfile = dir + "/" + file
    table = aws.detectDocumentTable(inputfile)
    filename, fileExtension = os.path.splitext(file)
    outputfile = self.tablesDirectory + "/"+ filename + ".txt"  
    writeFileJson(table,outputfile)
    return table


  def readText(self,file):
    filename, fileExtension = os.path.splitext(file)
    textfile = self.textDirectory+ "/"+ filename + ".txt"  
    return readFile(textfile)
    

  def readEntities(self,file):
    filename, fileExtension = os.path.splitext(file)
    textfile = self.entitiesDirectory + "/"+ filename + ".txt"  
    return readFileJson(textfile)
  
  
  def readTable(self,file):
    filename, fileExtension = os.path.splitext(file)
    table = self.tablesDirectory + "/"+ filename + ".txt"  
    return readFileJson(table)