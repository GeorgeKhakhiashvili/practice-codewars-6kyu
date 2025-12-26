#bit count
#ბინალურ ციფრებში არსებული 1იანების ჯამი
def bit_count(x):
    #ვაქცევთ მოცემულ ციფრს ბინალურად
    #we get bin form of provided numbers
    binaluri = bin(x)
    #ჯამი
    #sum
    sum_of_bin = 0
    #იტერაცია
    #iterating
    for i in binaluri:
        #ვეძებთ ერთიანებს თითვეულ ციფრში
        #getting all the '1' in bin form of i
        if i == "1":
            #ვაქცევდ ინტად და ვკრიბავთ
            sum_of_bin += int(i)
    #აბრუნებს პასუხს
    return sum_of_bin
print(bit_count(1234))
