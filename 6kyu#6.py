#გვაქ გასასეირნებლად დრო 10 წუთი და თითეული წუთი უდრის თითო ნაბიჯს,
#გვაქ დასავლეთი,აღმოსავლეთი, ჩრდილოეთი და სამხრეთი
#ჩვენი მისაა ისე წავიდეთ და წამოვიდეთ რომ სადაც ვართ იქ დავბრუნდეთ
def Take_a_Ten_Minutes_Walk(walk):
    #აუცილებელია დასავლეთის და აღმოსავლეთის ნაბიჯების რაოდენობა ემთვეოდეს,
    #ისევე როგორც ჩრდილოეთის და აღმოსავლეთის
    #ხოლო იფ დებულება ამოწმებს ამ ყოველივეს
    #steps should be equal(west steps should be same as east aswell as notrth and south)
    #if statemant checks that for us
    if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'):
        #მართალია და მცდარიათი ვამოწმებთ პასუხს
        #true and false for final answer
        return True
    else:
        return False
print(Take_a_Ten_Minutes_Walk(['n','n','n','s','n','s','n','s','n','s']))
