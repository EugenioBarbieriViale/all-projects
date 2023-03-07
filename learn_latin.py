import pandas, random

file = pandas.read_csv("words.csv")
file.columns = file.columns.str.normalize('NFKD').str.encode('ascii',errors='ignore').str.decode('utf-8')

latin_words = file.loc[:, "lemma"]
italian_words = file.loc[:, "traduzione"]

while True:
    n = random.randint(0, len(latin_words))

    if not pandas.isnull(latin_words[n]):
        inp = str(input("What's the translation of ({})?: ".format(latin_words[n])))
        print(italian_words[n])

        if inp not in italian_words[n]:
            print("WRONG")
        else:
            print("RIGHT")

        print()
