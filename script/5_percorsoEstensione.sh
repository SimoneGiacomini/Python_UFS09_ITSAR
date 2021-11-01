#!/bin/bash
#Scrivere uno script che riceve in input due parametri: un
#percorso e una estensione e indica quanti file ci sono di quel
#tipo
echo "Questo programma dopo che hai inserito un percorso ed un estensione, indica quanti file hai al suo interno"
echo "inserisci il percorso : "
read percorso
echo "inserisci un estensione, senza punto!"
read estensione
cd $percorso
file_da_cercare="${estensione}"
risultato=($(ls| grep $file_da_cercare))

echo " ci sono ${#risultato[@]} file con estensione ${estensione} "
