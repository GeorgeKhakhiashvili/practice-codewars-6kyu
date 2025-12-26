#წინადადების სიტყვებში არსებული ციფრების მიხედვით დალაგება
#sorting the words by numbers in it
def Your_order_please(txt):
    #ფუნქციაში ჩაშენებული ფუნქცია, რომელიც პოულობს ციფრებს თითვეულ სიტვაში
    #function inside function to find numbers in every word
    def find_digit(word):
        for char in word:
            if char.isdigit():
                return int(char)
    #ვაცალკევებთ სიტყვებს
    #seperating words
    words = txt.split()
    #ვალაგებთ სიტყვებს ციფრების ზრდადობის მიხედვით
    #sorting words by rank orfer of numbers
    sorted_words = sorted(words, key=find_digit)
    #ვაერთებთ ყველა სიტყვას რომ შევქმნათ წინადადება
    #sticking words to make sentence
    return " ".join(sorted_words)
print(Your_order_please("is2 Thi1s T4est 3a"))
