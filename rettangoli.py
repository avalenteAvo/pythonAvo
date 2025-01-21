#esercizio 6 cap 1 'Python e machine learning'

def rettangoli(riga,colonna):
    for i in range(riga): 
        if i<=0 or i>=riga-1:
            for k in range(colonna): print('*', end='')
            print()        
        else:
            for k in range(colonna):
                if(k<=0 or k>=colonna-1):print('*', end='')
                else: print('Q', end = '')
            print()
    return 

riga = int(input('Inserisci il numero delle righe del rettangolo: '))
colonna = int(input('Inserisci il numero delle colonne del rettangolo: '))
rettangoli(riga,colonna)

