#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv
import os
import fnmatch
import re

ftime = open('data/time.csv','w')
ftime.write("N,Time,Type\n")

# Traverses all the files
for filename in os.listdir("./data/"):
    filetype = None
    if (fnmatch.fnmatch(filename,"ftpdata*.csv")): filetype = "ftp"
    if (fnmatch.fnmatch(filename,"httpdata*.csv")): filetype = "http"
    if (fnmatch.fnmatch(filename,"httpsdata*.csv")): filetype = "https"
    if (filetype == None): continue
    filename = "./data/" + filename
    
    # Computes total time
    with open(filename, 'rt', encoding='utf8') as csvfile:
        print(filename)
        idn = int(re.search(r'\d+', filename).group())
        time = 0

        datareader = csv.reader(csvfile, delimiter=',')
        next(datareader, None) # Skips the header            
        for row in datareader:
            mins,secs = row[0].split('m')        
            mins = float(mins)
            secs = float(secs[:-1])
            time = time + mins*60 + secs

        ftime.write("{0},{1},{2}\n".format(idn,time,filetype))

ftime.close()        
