#!/usr/bin/env python3

import sys

fn=sys.argv[1]


def sopchk(line):
    idx=0
    while idx<(len(line)-4):
        piece=line[idx:idx+4]
        uniq=[]
        for a in piece:
            if a not in uniq: uniq.append(a)
        if len(uniq)==4:
            return idx+4
        idx+=1


if __name__=="__main__":
    with open(fn,"r") as fh:
        line=fh.read()

    idx=sopchk(line)
    print(idx)
