#!/bin/bash
DATAFILE=ftpdata.csv

echo -e "MBs,B" > $DATAFILE
wget -r ftp://localhost/bach --user=$1 --password=$2 2>&1 | grep saved | cut -f3,8 -d' ' | tr -d '([]' | tr ',' '.' | tr ' ' ',' >> $DATAFILE
