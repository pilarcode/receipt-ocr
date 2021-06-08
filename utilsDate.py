import dateparser
from utilsRegex import *
from utilsPrice import *


def isDate(token): 
  try:
    if isNumber(token):
      return False  
    if isText(token):
      return False
    if isPrice(token):
      return False
    if re.search(r'\n',token):
      return False
    date = dateparser.parse(token)
    return date!=None
  except (ValueError, TypeError):
    return False

def formatDate(token):
  token = token.replace("#","")
  datetime = dateparser.parse(token)
  return str(datetime.date())