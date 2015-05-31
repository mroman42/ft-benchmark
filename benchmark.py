#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import subprocess
import getpass
DEVNULL = open(os.devnull, 'w')


# Parsing script arguments
import argparse
parser = argparse.ArgumentParser(description='A file transmission protocol benchmark')
parser.add_argument('-u','--user', help='User executing wget (required in ftp)', required=True)
parser.add_argument('-p','--pass', help='Password for that user', required=False)
parser.add_argument('-i','--iterations', help='Number of iterations', required=False)
args = vars(parser.parse_args())
user = args['user']
pasw = args['pass']
nitr = args['iterations']
print("Executing benchmark with user: " + user)

if (pasw == None):
    print("Password for " + user + " is required to use ftp.")
    pasw = getpass.getpass()

if (nitr == None):
    nitr = 1
nitr = int(nitr)


# Benchmarking
for i in range(nitr):
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

    os.system("rm -rf localhost")
    print("[{0}] Executing FTP Benchmark...".format(idn))
    subprocess.call(["./download.sh", "ftp://localhost/bach", user, pasw, ftpdata])

    os.system("rm -rf localhost")
    print("[{0}] Executing HTTP Benchmark...".format(idn))
    subprocess.call(["./download.sh", "http://localhost/bach", user, pasw, httpdata])

    os.system("rm -rf localhost")
    print("[{0}] Executing HTTPS Benchmark...".format(idn))
    subprocess.call(["./download.sh", "https://localhost/bach", user, pasw, httpsdata])



# Timing
print("Computing total time...")
os.system("python3 timer.py")
print("ANOVA and LSD tests...")
os.system("Rscript stat.r")
print("Pandoc output formatting...")
os.system("pandoc results.md -o results.pdf")
