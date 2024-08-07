def contaore (a):
    b = a.split (', ')
    for x in range(len(b)):
        if b[x] == 'Dalle 10 alle 12':
            b[x] = '1'
            x +=1
        if b[x] == 'Dalle 14 alle 16':
            b[x] = '2'
            x +=1
        if b[x] == 'Dalle 16 alle 18':
            b[x] = '3'
            x +=1
        if b[x] == 'Dalle 18 alle 20':
            b[x] = '4'
            x +=1
        if b[x] == 'Dalle 20 alle 23':
            b[x] = '5'
            x +=1
    return b

