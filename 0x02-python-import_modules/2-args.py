#!/usr/bin/python3
from sys import argv
#arg = sys.argv[0:]
n = len(argv)
if n == 1:
    print ("0 arguments.")
elif n == 2:
    print ("{} argument:" .format(n - 1))
    print ("{}: {}".format(1, argv[1]))
else:
        print ("{} arguments:" .format(n - 1))
        for i in range(1, n):
            print ("{}: {}".format(i, argv[i]))
