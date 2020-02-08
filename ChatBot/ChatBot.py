import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy
import tensorflow
# import tflearn
import random

import json

with open('intents.json', 'r') as file:
    data = json.load(file)

words = []
lables = []
docs_x = []
docs_y= {}

for intent in data['intents']: