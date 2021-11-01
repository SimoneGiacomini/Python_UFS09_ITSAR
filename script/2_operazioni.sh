#!/bin/bash
#Scrivere uno script shell che riceve input 2 parametri a e b e
#visualizza i risultati delle seguenti operazioni:

echo "Questo programma prende in input 2 parametri e fa la SOMMA, SOTTRAZIONE, MOLTIPLICAZIONE, DIVISIONE"
echo "Inserisci il primo parametro: "
read a
echo "Inserisci il secondo parametro: "
read b

somma=$(($a+$b))
sottrazione=$(($a-$b)) 
moltiplicazione=$(($a*$b))
if [[ $b -eq 0 ]] ; then #-eq
	divisione="impossibile"
else
	divisione=$(($a/$b))
fi
echo "LA SOMMA è "
echo $somma
echo "LA SOTTRAZIONE è "
echo $sottrazione
echo "LA MOLTIPLICAZIONE "
echo $moltiplicazione
echo "LA DIVISIONE "
echo $divisione


