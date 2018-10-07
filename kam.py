#http://cecilia-urbina.blogspot.com/2013/02/string-matching.html?m=1, 
#se le realizaron modificaciones al programa original
import sys

def kmp(P, T):
    m = 0 
    i = 0 
    pos = 0 
    l_p = len(P)
    l_t = len(T)
    if(l_t >= l_p):
        tabla = tabla_fallos(P)
        print ("La tabla de fallos es %s"  %tabla)
        while((m<l_t) and (i<=l_p)):
            if(P[i] == T[m+i]):
                if(i == (l_p-1)):
                    pos = pos + 1 
                    print ("Esta en la posicion %s"  %m)
                    return
                i= i+1
            else:
                m = m + i - tabla[i]
                if(i>0):
                    i = tabla[i]

def tabla_fallos(P):
    l_p = len(P)
    k = 0
    table = [0] * l_p
    for q in range(1, l_p):
        while P[k] != P[q] and k > 0:
            k = table[k - 1]
        if P[k] == P[q]:
            k += 1
        table[q] = k
    table.insert(0, -1)
    return table[:-1]

def main():
    """funcion principal
    """
    try:
        T = "aaaaaaaaab"
        P = "aaab"
    except:
        return
    print ("El texto es %s" %T)
    print ("La palabra a buscar es %s" %P)
    kmp(P, T)

main()


