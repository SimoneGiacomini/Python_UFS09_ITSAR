#!/bin/bash
#Scrivere uno script che verifica chi è l'utente connesso (whoami) e verifica se si trova nella
#propria home directory ($HOME), scrivendo su un file di log l'utente e la data odierna 

my_user=$(whoami)
echo "Ciao $my_user"
fold=$(pwd)
cd /g/Il\ mio\ Drive/Scripting\ UFS09/script
if [[ "$fold" = "$HOME" ]]; then
	touch log.txt
	to_insert="${my_user} $(date) nella cartella corretta"
	echo $to_insert
	echo $to_insert >>log.txt
else
	touch log.txt
	to_insert="${my_user} $(date) cartella errata"
	echo $to_insert
	echo $to_insert>>log.txt
fi



















