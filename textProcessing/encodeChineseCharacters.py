#! /usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division, print_function, unicode_literals
import codecs
from random import choice, shuffle
import sys

chrs = {}
with codecs.open("characterList.dat", "r", "UTF-8") as inF:
    for line in inF:
        line = line.strip()
        if line == "": continue
        a, b = line.split("\t")
        lst = chrs.get(a, [])
        lst.append(b)
        chrs[a] = lst

string = sys.argv[1].lower()
changed, string_ = True, string
while changed:
    keys, string_ = [key for key in chrs], string
    shuffle(keys)
    for key in keys:
        string_ = string_.replace(key, choice(chrs[key]), 1)
    changed = string != string_
    string = string_

print(string)
