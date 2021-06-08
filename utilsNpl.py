import spacy
from utilsRegex import *
from utilsDate import *

def getEntityCommercialItem(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        if "COMMERCIAL_ITEM" ==  ent.label_:
            return ent.text
    return 'None'

def hasEntityCommercialItem(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        if "COMMERCIAL_ITEM" ==  ent.label_:
            return True
    return False

def getEntityQuantity(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        if "QUANTITY" ==  ent.label_:
            return ent.text
    return 'None'

def hasEntityQuantity(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        if "QUANTITY" ==  ent.label_:
            return True
    return False

def getEntityCardinal(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        if "CARDINAL" ==  ent.label_:
            return ent.text
    return 'None'

def hasEntityCardinal(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        if "CARDINAL" ==  ent.label_:
            return True
    return False


def getEntityDate(text):
    words = text.split("\n")
    for item in words:
        if isDate(item):
            return item
    return 'None'


def getEntities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)

