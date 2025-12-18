#Array.diff
def unikaluri():
    a = [1,2,3,4,5]
    b = [1,3,5]
    Unique = []
    for num in a:
        if num not in b:
            Unique.append(num)
    return Unique
print(unikaluri())
