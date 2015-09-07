#!/usr/bin/env python3

import csv
import pickle

with open('baeume.csv', mode='r') as infile:
    reader = csv.reader(infile, delimiter=';')
    next(reader, None)  # skip the headers
    mydict = { rows[1]:rows[0] for rows in reader }
    with open('baeume.pickled', mode='wb') as outfile:
        pickle.dump(mydict, outfile, protocol=4)

#    print "mapping "+rows[1]+ " to "+rows[0]."\n"

#print(mydict['1'])
