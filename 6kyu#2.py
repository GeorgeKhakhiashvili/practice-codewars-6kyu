def unikaluri():
    #შემოგვაქ 3 სია, 2 სია შედარებისთვის, ხოლო მესამე uniqueში საბოლოოდ ვიღებთ პასუხს
    #we have 3 lists, 2 for comprasion and third one "the unique" to add final answer
    a = [1,2,3,4,5]
    b = [1,3,5]
    Unique = []
    #ვაკეთებთ იტერაციას პირველ ორ სიაზე
    #iterateing over lists
    for num in a:
        if num not in b:
            #ხოლო თუ ერთი პრიველი სიის ელემენტი მეორეში არ აღმოჩნდა ვიღებთ პასუხს
            #so if list a elment doesnt show up in list b function returs the unique element
            Unique.append(num)
    return Unique
print(unikaluri())
