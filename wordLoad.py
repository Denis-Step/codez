from nltk.corpus import wordnet as wn
import diego_query as db

with open('5lenwords.txt') as f:
    for line in f:
        word = line.strip()
        db.create_word(word)