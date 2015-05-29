#!/bin/bash

echo -e "MBs,B" > ftpresults.data
wget -r ftp://localhost/bach --user=$1 --password=$2 2>&1 | grep saved | cut -f3,8 -d' ' | tr -d '(','['.']' | tr ',' '.' | tr ' ' ',' >> ftpresults.data
