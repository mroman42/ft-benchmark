#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Computes total time
import csv

with open("data/ftpdata.csv", 'rt', encoding='utf8') as csvfile:
    time = 0
    datareader = csv.reader(csvfile, delimiter=',', )
    next(datareader, None) # Skips the header

    for row in datareader:
        mbps = float(row[0])
        byts = float(row[1])

        time = time + byts/(mbps*1024*1024)

print(time)

ftime = open('data/time.csv','w')
ftime.write("N,Time,Type\n")
ftime.write("{0},{1},{2}\n".format(1,time,"ftp"))
ftime.close()
