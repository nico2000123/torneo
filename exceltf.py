import settimana1
import contaore
import settimana2
def foo(a):
    prima = settimana1.settimana1(a[0])
    seconda = contaore.contaore(a[1])
    terza = settimana2.settimana2(a[2])
    quarta = contaore.contaore(a[3])
    lista = (prima,seconda,terza,quarta)
    return lista