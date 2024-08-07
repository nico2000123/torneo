def settimana2 (a):
    b = a.split (', ')
    for x in range(len(b)):
        if b[x] == 'Lunedì 19':
            b[x] = 'L'
            x +=1
        if b[x] == 'Martedì 20':
            b[x] = 'Ma'
            x +=1
        if b[x] == 'Mercoledì 21':
            b[x] = 'Me'
            x +=1
        if b[x] == 'Giovedì 22':
            b[x] = 'G'
            x +=1
        if b[x] == 'Venerdì 23':
            b[x] = 'V'
            x +=1
        if b[x] == 'Sabato 24':
            b[x] = 'S'
            x +=1
        if b[x] == 'Domenica 25':
            b[x] = 'D'
            x +=1
            
    return b

