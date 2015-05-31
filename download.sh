#!/bin/bash

echo -e "Time(ms)" > $4
{ time wget -r $1 --user=$2 --password=$3 --no-check-certificate 2>&1; } |& grep real | tr -d "real \t" >> $4
