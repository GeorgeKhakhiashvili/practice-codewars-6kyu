#Find the odd int
def odd(list):
    for num in list:
        if list.count(num) % 2 != 0:
            return num, "number is odd"
print(odd([1,2,2,3,3,3,4,3,3,3,2,2,1]))
