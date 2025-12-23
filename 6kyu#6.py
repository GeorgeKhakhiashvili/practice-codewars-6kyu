def Take_a_Ten_Minutes_Walk(walk):
    if walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'):
        return True
    else:
        return False
print(Take_a_Ten_Minutes_Walk(['n','n','n','s','n','s','n','s','n','s']))
