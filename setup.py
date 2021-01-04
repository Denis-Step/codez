from nltk.corpus import wordnet as wn
import models

if __name__ == "__main__":
    models.db.create_all()

    first_user_creds = models.User.hash_password(b"TESTING")
    test_user = models.User(
        id=0,
        name="Dummy",
        email="fake@gmail.com",
        password=first_user_creds["hashed_pw"],
        salt=first_user_creds["salt"],
        gamesPlayed=0,
        gamesWon=0,
    )
    models.db.session.add(test_user)
    models.db.session.commit()

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
