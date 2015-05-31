#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import subprocess
DEVNULL = open(os.devnull, 'w')


# Parsing script arguments
import argparse
parser = argparse.ArgumentParser(description='A file transmission protocol benchmark')
parser.add_argument('-u','--user', help='User executing wget', required=True)
parser.add_argument('-p','--pass', help='Password for that user', required=True)
args = vars(parser.parse_args())
user = args['user']
pasw = args['pass']
print("Executing benchmark with user: " + user)


# Benchmark id number
idn = 0
while (os.path.isfile("data/ftpdata{0}.csv".format(idn)) 
       or os.path.isfile("data/httpdata{0}.csv".format(idn)) 
       or os.path.isfile("data/httpsdata{0}.csv".format(idn))):
    idn = idn + 1


# Benchmarks
ftpdata = "data/ftpdata{0}.csv".format(idn)
httpdata = "data/httpdata{0}.csv".format(idn)
httpsdata = "data/httpsdata{0}.csv".format(idn)

print("Executing FTP Benchmark...")
subprocess.call(["./download.sh", "ftp://localhost/bach", user, pasw, ftpdata])
print("Executing HTTP Benchmark...")
subprocess.call(["./download.sh", "http://localhost/bach", user, pasw, httpdata])
print("Executing HTTPS Benchmark...")
subprocess.call(["./download.sh", "https://localhost/bach", user, pasw, httpsdata])
