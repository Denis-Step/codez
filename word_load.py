from nltk.corpus import wordnet as wn
import modelmethods as db


with open('5lenwords.txt') as f:
    counter = 0
    for line in f:
        counter += 1
        word=line.strip()
        try:
            db.create_word(word, counter)
        except Exception:
            continue
