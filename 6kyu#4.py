#bit count
def bit_count(x):
    binaluri = bin(x)
    sum_of_bin = 0
    for i in binaluri:
        if i == "1":
            sum_of_bin += int(i)
    return sum_of_bin
print(bit_count(1234))
