#!/bin/bash
#Si realizzi uno script “scriviNumeri.sh” che scrive a video i
#numeri da 0 a N: 0,1,2,..........,N-1
#Il valore di N viene passato allo script da riga di comando.
#Esempio di lancio: $ ./scriviNumeri.sh N

for (( i = 0 ; i < $1 ; i += 1 )) ; do
echo  $i
done
