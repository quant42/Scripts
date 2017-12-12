#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division, print_function
from Bio import SeqIO
import sys

getName = lambda x : x if "_" not in x else x[:x.rfind("_")]
data = {}

with open(sys.argv[1], "r") as inF:
    for record in SeqIO.parse(inF, "fasta"):
        fullName = record.name
        name = getName(fullName)
        seq = str(record.seq)
        data[name] = data.get(name, [])
        data[name].append((fullName, seq))

with open(sys.argv[2], "w") as outF:
    for key in data:
        lst = data[key]
        if len(lst) == 1:
            name, seq = lst[0]
            outF.write(">")
            outF.write(name)
            outF.write("_1\n")
            outF.write(seq)
            outF.write("\n")
            name, seq = lst[0]
            outF.write(">")
            outF.write(name)
            outF.write("_2\n")
            outF.write(seq)
            outF.write("\n")
        elif len(lst) == 2:
            name1, seq1 = lst[0]
            name2, seq2 = lst[1]
            if seq1 == seq2:
                outF.write(">")
                outF.write(name1)
                outF.write("\n")
                outF.write(seq1)
                outF.write("\n")
                outF.write(">")
                outF.write(name2)
                outF.write("\n")
                outF.write(seq2)
                outF.write("\n")
            else:
                outF.write(">")
                outF.write(name1)
                outF.write("\n")
                outF.write(seq1)
                outF.write("\n")
                outF.write(">")
                outF.write(name1)
                outF.write("\n")
                outF.write(seq1)
                outF.write("\n")
                outF.write(">")
                outF.write(name2)
                outF.write("\n")
                outF.write(seq2)
                outF.write("\n")
                outF.write(">")
                outF.write(name2)
                outF.write("\n")
                outF.write(seq2)
                outF.write("\n")
        else:
            print("WARNING: More than 2 sequences found for individual '%s'" % key)
            for name, seq in lst:
                outF.write(">")
                outF.write(name)
                outF.write("\n")
                outF.write(seq)
                outF.write("\n")
