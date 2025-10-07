#!/bin/bash

URL="https://parcari.adp-sector1.ro/"

response=$(curl -s -w "%{http_code}" $URL)

sc=$(tail -n1 <<< "$response")  # get the last line
#content=$(sed '$ d' <<< "$response")   # get all but the last line which contains the status code

if [ $sc -lt 200 ]; || if [ $sc -gt 300 ]; then
    echo "Site is still DOWN"
else
    echo "Site is UP"

fi

echo $sc