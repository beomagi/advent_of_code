#!/usr/bin/env python3

import sys

fn=sys.argv[1]


stacks={}

def loadcrates(line):
    idx=1
    while len(line)>0:
        if idx not in stacks: stacks[idx]=[]
        crate=line[:4]
        line=line[4:]
        if "[" in crate:
            crate=crate.replace(" ","").replace("[","").replace("]","")
            stacks[idx].append(crate)
        idx+=1

def finishload():
    global stacks
    for idx in stacks:
        stacks[idx].reverse()


def domove(aline):
    global stacks
    ins=aline.split(" ")
    cnt=int(ins[1])
    src=int(ins[3])
    dst=int(ins[5])
    temp=[]
    while cnt>0:
        crate=stacks[src].pop()
        temp.append(crate)
        cnt-=1
    while len(temp)>0:
        crate=temp.pop()
        stacks[dst].append(crate)

if __name__=="__main__":
    with open(fn,"r") as fh:
        lines=fh.read()
    linesep=lines.split("\n")

    count=0
    cratelayout=[]
    for aline in linesep:
        if "[" in aline:
            loadcrates(aline)
        if " 1   2  " in aline:
            finishload()
        if "move" in aline:
            domove(aline)

    #print(stacks)
    fnal=""
    for idx in stacks:
        fnal+=stacks[idx].pop()
    print(fnal)
