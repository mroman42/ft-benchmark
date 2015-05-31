import os

nfiles = 333
tsize = 3*1024*1024*1024
fsize = int(tsize/nfiles)

print ("Creating random test files in ./bach/")

if not os.path.exists("bach"):
    os.makedirs("bach")

for i in range(333):
    with open("bach/test"+str(i), 'wb') as fout:
        fout.write(os.urandom(fsize))
