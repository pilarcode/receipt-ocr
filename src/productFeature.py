import re
from src.utilsRegex import isNumber,isProductDescription
from src.utilsPrice import isPrice,formatPrice

class ProductFeature:

  def __init__(self,dic, lines):
    self.dic = dic
    self.lines = lines
   
  def process(self):
    items = {}
    if bool(self.dic) :
      items= self.extractItemsFromTable(self.dic)
      
    if bool(items) == False:
      items = self.extractItemsFromLines(self.lines)
    return items

  def extractItemsFromLines(self, list):
    items = {} 
    for index, value in enumerate(list):
      current = value
      previous = list[index-1]
      if isPrice(current) and self.isProduct(previous):
        if self.isTotal(previous):
          return items
        else:
          item_name = previous
          item_price = value
          items[item_name] = formatPrice(item_price)
  
    return items

  def extractItemsFromTable(self, dic):
    items = {}
    for index, key in enumerate(dic):
      item_name =  key
      item_price = dic[key]
      if self.isTotal(item_name) == False and self.isProduct(item_name) and isPrice(item_price):
        item_name = item_name 
        items[item_name] = formatPrice(item_price)
    return items

  def isTotal(self,token):
    if re.search('TOTAL',token.upper()):
      return True
    if re.search('SUBTOTAL',token.upper()):
      return True
    if re.search('CASH',token.upper()):
      return True
    if re.search('CARD',token.upper()):
      return True 
    if re.search('CHANGE',token.upper()):
      return True
    if re.search('TAX',token.upper()):
      return True
    if re.search('DUE',token.upper()):
      return True
    if re.search('GST',token.upper()):
      return True
    if re.search('ROUND OFF',token.upper()):
      return True
    if re.search('AMOUNT',token.upper()):
      return True
    if re.search('CHARGE',token.upper()):
      return True
    if re.search('SUMMA',token.upper()):
      return True
    return False

  def isProduct(self,token):
      if isProductDescription(token):
        return True
      return False

  def formatProduct(self,token):
    product =''
    words = token.split(" ")
    for item in words:
      if isNumber(item) == False:
        product += item + " "
    return product
  
 

    