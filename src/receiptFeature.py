#from platform import processor
from src.utilsAws import detectDocumentText,detectEntitiesFromText,detectDocumentTable
from src.utilsFile import readFileJson,writeFileJson,writeFile,readFile
from src.dateFeature import DateFeature
from src.productFeature import ProductFeature
from src.shopFeature import ShopFeature
import os

class ReceiptFeature:

  def __init__(self):
    self.textDirectory = 'src/text'
    self.entitiesDirectory = 'src/entidades'
    self.tablesDirectory ='src/tables'
    self.tmpDirectory ="src/tmp"
  
  
  def getFeatures(self, file):
  
    print("Procesando el fichero: {}".format(file))
    text = self.saveTextDetectedByTextract(self.tmpDirectory,file)
    entities=self.saveEntitiesDetectedByComprehed(self.entitiesDirectory,file,text)
    table = self.saveTableDetectedByTextract(self.tmpDirectory,file)
    
    text = self.readText(file)
    table = self.readTable(file)
    entities = self.readEntities(file)  
    
    features = {}
    extractor = ShopFeature(entities,text)
    features['shop'] = extractor.process()
    extractor = DateFeature(entities)
    features['date']  = extractor.process()
    extractor = ProductFeature(table,text)
    features['items'] = extractor.process()
    return features

  def saveTextDetectedByTextract(self,dir,file):    
    inputfile = dir + "/" + file
    text = detectDocumentText(inputfile)
    filename, fileExtension = os.path.splitext(file)
    outputfile = self.textDirectory + "/"+ filename + ".txt"  
    writeFile(text,outputfile)
    return text
      
  def saveEntitiesDetectedByComprehed(self,dir,file,text):
    entities = detectEntitiesFromText(text)
    filename, fileExtension = os.path.splitext(file)
    outputfile = dir + "/"+ filename + ".txt"  
    writeFileJson(entities,outputfile)
    return entities
  
  def saveTableDetectedByTextract(self, dir, file):
    inputfile = dir + "/" + file
    table = detectDocumentTable(inputfile)
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