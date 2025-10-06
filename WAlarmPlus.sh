#!/usr/bin/bash

URL="https://parcari.adp-sector1.ro/"
title="Primaria Secotor 1 Parcari"
min_size=1024

response=$(curl -s -w "%{http_code}" $URL)
sc=$(tail -n1 <<< "$response")  
size=$(curl -s -w "%{size_download}" $URL)
body=$(curl -s $URL)

if [ $sc -lt 200 ] || [ $sc -gt 300 ]; then
    echo "Site is still DOWN"
elif [ $size -lt $min_size ]; then
    echo "Site loaded but something is wrong, maybe error"
elif [ $( grep -q 'title' <<<$body; echo $?) -eq 1 ]; then
    echo "Site loaded but something is wrong, maybe wrong page"
else
    echo "Site is UP for real" 
    echo -en "\007"
    echo 'message:Site is UP' | zenity --notification --listen  
fi
echo $sc