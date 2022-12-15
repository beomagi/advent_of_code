#!/usr/bin/env python3

import sys

fn=sys.argv[1]


def linesto2da(lines):
    treearray=[]
    for line in lines:
        if line.strip()!="":
            treeline=[]
            for char in line:
                treeline.append(int(char))
            treearray.append(treeline)
    return treearray


def visiblescore(treearray,x,y,width,height):
    curheight=treearray[y][x]
    vx=x
    vy=y-1
    seen_up=0
    while vy>=0:
        seen_up+=1
        if treearray[vy][vx]>=curheight:
            break
        vy=vy-1

    vx=x
    vy=y+1
    seen_dn=0
    while vy<height:
        seen_dn+=1
        if treearray[vy][vx]>=curheight:
            break
        vy+=1

    vx=x-1
    vy=y
    seen_lt=0
    while vx>=0:
        seen_lt+=1
        if treearray[vy][vx]>=curheight:
            break
        vx-=1

    vx=x+1
    vy=y
    seen_rt=0
    while vx<height:
        seen_rt+=1
        if treearray[vy][vx]>=curheight:
            break
        vx+=1

    visible=seen_up * seen_dn * seen_lt * seen_rt
    return visible




if __name__=="__main__":
    with open(fn,"r") as fh:
        data=fh.read()
    lines=data.split("\n")

    treearray=linesto2da(lines)

    height=len(treearray)
    width=len(treearray[0])

    maxviz=0
    for x in range(width):
        for y in range(height):
            score=visiblescore(treearray,x,y,width,height)
            maxviz=max(maxviz,score)
    print(maxviz)
