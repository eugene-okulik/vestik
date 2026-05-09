lorem_ipsum = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
               'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

words = lorem_ipsum.split()
fin_words = []
for word in words:
    if word[-1] == ',' or word[-1] == '.':
        fin_words.append(word[:-1] + 'ing' + word[-1])
    else:
        fin_words.append(word + 'ing')

print(' '.join(fin_words))
