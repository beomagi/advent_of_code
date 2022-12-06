#!/usr/bin/env python3

import sys

fn=sys.argv[1]

if __name__=="__main__":
    with open(fn,"r") as fh:
        lines=fh.read()

    linesep=lines.strip().split("\n")

    count=0
    for aline in linesep:
        ranges=aline.split(",")
        r1=ranges[0].split("-")
        r2=ranges[1].split("-")
        r1[0]=int(r1[0])
        r1[1]=int(r1[1])
        r2[0]=int(r2[0])
        r2[1]=int(r2[1])
        overlap=0
        if r1[0]>=r2[0] and r1[0]<=r2[1]: overlap=1
        if r2[0]>=r1[0] and r2[0]<=r1[1]: overlap=1
        if r1[1]>=r2[0] and r1[1]<=r2[1]: overlap=1
        if r2[1]>=r1[0] and r2[1]<=r1[1]: overlap=1
        count+=overlap
        print("{}  \t{}  {}".format(aline, overlap, count))

    print(count)

