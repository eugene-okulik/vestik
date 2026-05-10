words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def repeat_words(word, number):
    result = word * number
    print(result)

for word, number in words.items():
    repeat_words(word, number)
