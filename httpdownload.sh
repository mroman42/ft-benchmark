#!/bin/bash
DATAFILE=httpdata.csv

echo -e "MBs,B" > $DATAFILE
wget -r http://localhost/bach --user=$1 --password=$2 2>&1 | grep saved | cut -f3,8 -d' ' | tr -d '([]' | tr ',' '.' | tr ' ' ',' | cut -f1 -d'/' >> $DATAFILE
