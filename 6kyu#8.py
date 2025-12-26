def Your_order_please(txt):
    def find_digit(word):
        for char in word:
            if char.isdigit():
                return int(char)
    
    words = txt.split()
    sorted_words = sorted(words, key=find_digit)
    return " ".join(sorted_words)
print(Your_order_please("is2 Thi1s T4est 3a"))
