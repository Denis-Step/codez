from nltk.corpus import wordnet as wn
import models


def setup_db():
    models.db.create_all()
    test_user = models.User.create(
        username="Dummy", email="fake@gmail.com", password="TESTING"
    )

    with open("models/5lenwords.txt") as f:
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


if __name__ == "__main__":
    setup_db()