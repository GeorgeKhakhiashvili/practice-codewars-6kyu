def ragaca(txt):
    saparated_list = txt.split()
    new_list = []
    for word in saparated_list:
        if len(word) >= 5:
            reversed_word = word[:: -1]
            new_list.append(reversed_word)
        elif len(word) <= 4:
            new_list.append(word)
    return " ".join(new_list)
print(ragaca("you will never walk alone"))