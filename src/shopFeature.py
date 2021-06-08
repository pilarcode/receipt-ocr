from src.utilsRegex import isText,isNumber

class ShopFeature:
  
  def __init__(self,entities,text):
    self.entities = entities
    self.text = text


  def process(self):
    firstLine = self.extractShopName(self.text)
    
    # organization=''
    # if 'ORGANIZATION' in self.entities:
    #   tokens = self.entities['ORGANIZATION']
    #   for token in tokens:
    #     if organization=='' and isAlphaNumeric(token):
    #       organization = token
    #       break
    #if organization in firstLine and len(firstLine)> len(organization):
    #  return firstLine
    return firstLine
    

  def extractShopName(self, text):
    for token in text:
      if self.isShop(token):
        return token
    return 'None'
  
  def isShop(self,token):
    copy = token
    copy = copy.replace(",","")
    copy = copy.replace("-","")
    copy = copy.replace(".","")
    copy = copy.replace("_","")
    copy = copy.replace("'","")
    if isText(copy) and not isNumber(copy):
      return True
    return False

