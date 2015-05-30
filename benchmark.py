#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import subprocess
DEVNULL = open(os.devnull, 'w')

# Argumentos al script
import argparse
parser = argparse.ArgumentParser(description='A file transmission protocols benchmark')
parser.add_argument('-u','--user', help='User executing wget', required=True)
parser.add_argument('-p','--pass', help='Password for that user', required=True)
args = vars(parser.parse_args())
user = args['user']
pasw = args['pass']

print("Executing benchmark with user: " + user)

# Comando para la transmisión por ftp
subprocess.call(["./ftpdownload.sh", user, pasw])
