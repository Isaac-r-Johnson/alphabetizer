def convert_list_to_string(li):
    string = ''
    return string.join(li)


words = []
word = ''

while word != 'done':
    word = input("Type Word: ")
    word = word.lower()
    if word != 'done':
        words.append(word)
words.sort()

for word in words:
    word_num = words.index(word) + 1
    word = list(word)
    word[0] = word[0].upper()
    word = convert_list_to_string(word)
    print(f"{word_num}. {word}")



