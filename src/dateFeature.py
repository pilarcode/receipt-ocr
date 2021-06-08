from src.utilsNpl import getEntityDate
from src.utilsDate import formatDate,isDate

class DateFeature:

  def __init__(self,entities):
    self.entities = entities
  
  def sortByLen(self, input):
    output = sorted(input.copy(), key=len)
    return output

  def process(self):
    if 'DATE' in self.entities:
      tokens = self.entities['DATE']
      tokens = self.sortByLen(tokens)    
      for token in reversed(tokens):
        if isDate(token) :
          return formatDate(token)
        else:
          value = getEntityDate(token)
          if value!='None':
            return formatDate(value)  
   
    return None
  

    

