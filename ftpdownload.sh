#!/bin/bash

echo -e "MBs,B" > $4
wget -r $1 --user=$2 --password=$3 2>&1 | grep saved | cut -f3,8 -d' ' | tr -d '([]' | tr ',' '.' | tr ' ' ',' >> $4
