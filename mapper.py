#!/usr/bin/python

import sys
import ast
for line in sys.stdin:
        line = line.strip()
        words=line.split('\t')
        data = ast.literal_eval(words[04])
        try:
                p = data["subjects"]
        except KeyError:
                p = ""
                pass
        for q in p:
                print "%s\t\t%s" %(q,1)
