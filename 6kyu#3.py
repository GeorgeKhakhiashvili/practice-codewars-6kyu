#Find the odd int
def odd(list):
    #იტერაცია ლისტზე
    #iterating over list
    for num in list:
        #ვეძებთ ლისტში იმ ელემნტს რომლის რაოდენობა კენტია
        #searching  amount of elemnt in list which is odd
        if list.count(num) % 2 != 0:
            #ვიღებთ სასურველ პასუხს
            #we get our answer
            return num, "number is odd"
print(odd([1,2,2,3,3,3,4,3,3,3,2,2,1]))
