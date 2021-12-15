#!/usr/bin/env python3

import sys

def reducer_max():
    MaxSales = []
    oldKey = None

    for line in sys.stdin:
        data = line.strip().split(",")

        thisKey, thisCost = data
        if oldKey is not None and oldKey != thisKey:
            print(oldKey + "," + str(max(MaxSales))
            MaxSales = []

        oldKey = thisKey
        MaxSales.append(float(thisCost))

    if oldKey is not None: # for the final key
        print (oldKey + "," + str(max(MaxSales)))

if __name__ == "__main__":
    # what function should run when python reducer_max.py is called?
    reducer_max()
