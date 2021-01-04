from nltk.corpus import wordnet as wn
import models

if __name__ == "__main__":
    with open("5lenwords.txt") as f:
        counter = 0
        for line in f:
            counter += 1
            word = line.strip()
            try:
                new_word = models.Word(word=word, wordid=counter)
                models.db.session.add(new_word)
                models.db.session.commit()
            except Exception:
                print("exception")
                continue
