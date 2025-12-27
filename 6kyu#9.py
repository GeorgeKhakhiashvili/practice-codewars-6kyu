#განსაკუთრებული რჩება ერთხელ
def unique_in_order(txt):
    #შემოგვაქ ორი ცვლადი ერთი საბოლოო შედეგის ხოლო მეორე იმ ელემნტისთვის რომელიც არ გვინდა რომ გამეორდეს
    #we get two variables one for result and second one for the element which we dont want to reappend
    result = []
    prev = 0
    for i in txt:
        #აღნიშნული იფ მოთოვნით ჩვენი ელემნტი არ გამეორდება
        #with this if statement our element wont reappend
        if i != prev:
            #პირველრიგში დაემატება პირველი ელემენტი ხოლო, შემდეგ პირველს ვანიჭბეთ წინას სახელს
            #first element will be appended and then we give first value of previous so it wont reappend
            result.append(i)
            prev = i
    return result
print(unique_in_order(('AAAABBBCCDAABBB')))
