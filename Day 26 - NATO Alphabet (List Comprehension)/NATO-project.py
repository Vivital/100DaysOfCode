import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
print(phonetic_dictionary)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [phonetic_dictionary[letter] for letter in word]
    except KeyError:
        print("Please enter the letters")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()
