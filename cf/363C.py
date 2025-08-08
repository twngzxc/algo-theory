word = str(input())
consecutive_letter = False
couple = 0
break1 = False
break2 = False
lst = [word[0]]
for i in range(1,len(word)):
    if word[i] != lst[-1]: # different letter from previous, just add
        lst.append(word[i])
        consecutive_letter = False
        if couple == 1:
            if break1:
                break2 = True   # second time diff
            break1 = True       # first time diff
            if break1 and break2:   # 2 time diff break the couple
                couple = 0 
    else:                       # same letter as previous
        if not consecutive_letter and couple == 0: # only got 1 letter and no couple right infront yet
            lst.append(word[i])
            consecutive_letter = True
            couple = 1
            break1 = False
            break2 = False
        elif not consecutive_letter and couple == 1: # only got 1 letter but there is couple right infront
            continue
        else: # got 2 letter
            continue
for i in range(len(lst)):
    print(lst[i], end = "")
