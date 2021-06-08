import re

def eliminarCaracteresEspeciales(token):
  chars = ["!",";","@","?","¿","¡","#","$","%","&","'","*","+","-","^","_","`","\|","~",":","/"]
  copy = token
  for i in chars:
    copy  = copy.replace(i,"")
  return copy

def isAlphaNumeric(token):
    if re.match(r'[a-zA-Z0-9 ]+', token):
      return True
    return False

def isProductDescription(token):
    if re.match(r'^[a-zA-Z]{3,25}.*', token):
      return True #SOPA 1
    if re.match(r'^[0-9]+ [a-zA-Z ]{2,25}.*', token):
      return True # 1 SOPA
    return False

def isNumber(token):
    if re.search(r'^\d{1,50}$',token):
      return True
    return False

def isFloat(value):
  try:
    float(value)
    return True
  except (ValueError, TypeError):
    return False

def isText(token):
    if re.match(r'^[a-zA-Z ]{2,100}$', token):
      return True
    return False

