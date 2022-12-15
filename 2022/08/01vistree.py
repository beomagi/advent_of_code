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


def isvisible(treearray,x,y,width,height):
    curheight=treearray[y][x]
    if x==0: return True
    if x==width-1: return True
    if y==0: return True
    if y==height-1: return True
    visible=False

    vx=x
    vy=y-1
    seen_up=True
    while vy>=0:
        if treearray[vy][vx]>=curheight:
            seen_up=False
            break
        vy=vy-1

    vx=x
    vy=y+1
    seen_dn=True
    while vy<height:
        if treearray[vy][vx]>=curheight:
            seen_dn=False
            break
        vy+=1

    vx=x-1
    vy=y
    seen_lt=True
    while vx>=0:
        if treearray[vy][vx]>=curheight:
            seen_lt=False
            break
        vx-=1

    vx=x+1
    vy=y
    seen_rt=True
    while vx<height:
        if treearray[vy][vx]>=curheight:
            seen_rt=False
            break
        vx+=1
    visible=seen_up or seen_dn or seen_lt or seen_rt
    return visible




if __name__=="__main__":
    with open(fn,"r") as fh:
        data=fh.read()
    lines=data.split("\n")

    treearray=linesto2da(lines)

    height=len(treearray)
    width=len(treearray[0])
    viscount=0
    for x in range(width):
        for y in range(height):
            if isvisible(treearray,x,y,width, height):
                viscount+=1
    print(viscount)
