def Narcissistic_Number(txt):
    new_txt = str(txt)
    power = len(new_txt)
    sum_of_nums = 0
    for i in new_txt:
        sum_of_nums += int(i)**power
    if sum_of_nums == int(txt):
        return True
    else:
        return False

print(Narcissistic_Number('999'))
