def settimana1 (a):
    b = a.split (', ')
    for x in range(len(b)):
        if b[x] == 'Lunedì 12':
            b[x] = 'L'
            x +=1
        if b[x] == 'Martedì 13':
            b[x] = 'Ma'
            x +=1
        if b[x] == 'Mercoledì 14':
            b[x] = 'Me'
            x +=1
        if b[x] == 'Giovedì 15':
            b[x] = 'G'
            x +=1
        if b[x] == 'Venerdì 16':
            b[x] = 'V'
            x +=1
        if b[x] == 'Sabato 17':
            b[x] = 'S'
            x +=1
        if b[x] == 'Domenica 18':
            b[x] = 'D'
            break
            
    return b