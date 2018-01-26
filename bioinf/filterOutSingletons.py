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
        seq = str(record.seq)
        l = data.get(seq, [])
        l.append(fullName)
        data[seq] = l

# now filter out all singletons
with open(sys.argv[2], "w") as outF:
    for seq in data:
        names = data[seq]
        indNames = set()
        for name in names:
            indNames.add(getName(name))
        if len(indNames) >= 2:
            for name in names:
                outF.write(">%s\n%s\n" % (name, seq))
