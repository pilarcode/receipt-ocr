import re

def isPrice(price):
    try:
      if re.match(r'\d+[.|,]\d{2}', price):
        return True # 12.00 
     
      if re.match(r'\d+[.|,]\d{2} *\$', price):
        return True  #12.00 $ 12.00$
     
      if re.match(r'[$] *\d+[.|,]\d{2}', price):
        return True  #$ 12.00 $12.00"
      
      if re.match(r'^\d+[.|,]\d{2} EUR', price):
        return True # 12.00 EUR

      if re.match(r'^\d+[.|,]\d{2} \€', price):
        return True # 12.00 €

      """ SR 12.00 SR12.00"""
    #  if re.match(r'[A-Z]{2,3} *\d+[.|,]\d{2}', price):
    #    return True
      """ 12.00SR 12,00 SR  12.00 S"""
    #  if re.match(r'\d+[.|,]\d{2} [A-Z]{1,3}', price):
    #    return True
      return False
    except(ValueError, TypeError):
      return False

def formatPrice(token):
    price =''
    for pos, c in enumerate(token):
      if re.match(r'\d', c)  or c == '.':
        price += c
      elif re.match(r'[a-zA-Z ]',c):
        return price
    return price