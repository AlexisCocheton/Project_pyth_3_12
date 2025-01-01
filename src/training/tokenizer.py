
def tokenize (text:str):
    a=[[text[0]+text[1],0]]
    for i in range(len(text)-1):
        cpt=0
        letter1 = text[i]
        letter2 = text[i+1] 
        token= letter1+letter2
        for j in range(len(a)):
            if a[j][0] == token:
                a[cpt][1] += 1
                break
            if j==(len(a)-1):
                a.append([token,1])
            cpt+=1
    return a
print(tokenize("la fleur du du printemps"))