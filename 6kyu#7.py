#ნარცისი რიცხვი/ციფრი მოცემული ციფრი უნდა ემთხვეოდეს ციფრში
#შემავალი ყველა ნაწილის კუბის ჯამს
def Narcissistic_Number(txt):
    #ვაქცევთ სტრინგად, რადგან სტრინგზე იტერაცია უფრო მარტივია
    #iterating over string is better
    new_txt = str(txt)
    #ვიგბთ მოცემული სრინგის ზომას, რომელიც იქნება ხარისხი
    #length of string will be power used later
    power = len(new_txt)
    #საბოლოო ჯამი
    #final answer
    sum_of_nums = 0
    for i in new_txt:
        #საბოლოო ჯამს ვუმატებთ ინტად გადაქცეულ ელენტს ხარისხად (სტრინგის ზომა)
        #we add sum_of_nums inted element in power of strings length
        sum_of_nums += int(i)**power
        #ვამოწმებთ მიღებული შედეგი თუ უდრის თვდაპირველ ციფრს/რიცხვს
        #checking if result and given number is same
    if sum_of_nums == int(txt):
        return True
    else:
        return False
print(Narcissistic_Number(999))
