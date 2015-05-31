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


# Benchmarks
ftpdata = "data/ftpdata.csv"
httpdata = "data/httpdata.csv"
httpsdata = "data/httpsdata.csv"

print("Executing FTP Benchmark...")
subprocess.call(["./ftpdownload.sh", "ftp://localhost/bach", user, pasw, ftpdata])
print("Executing HTTP Benchmark...")
subprocess.call(["./httpdownload.sh", "http://localhost/bach", user, pasw, httpdata])
print("Executing HTTPS Benchmark...")
subprocess.call(["./httpdownload.sh", "https://localhost/bach", user, pasw, httpsdata])
