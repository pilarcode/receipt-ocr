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