def Duplicate_Encoder (word):
    word = str.lower(word)
    return "".join(")"if word.count(ch) == 1 else "(" for ch in word)
print(Duplicate_Encoder("gioo"))
