#!/bin/bash
echo "Salut! Azi este $(date)"
echo "Vremea în Ploiesti:"
curl -s wttr.in/Ploiesti
exec "$@"