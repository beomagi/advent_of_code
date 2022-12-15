#!/usr/bin/env python3

import sys
import time
import os
from colorama import Fore, Back, Style

fn=sys.argv[1]



def putxy(x,y,t,col=""):
    print(col+"\033[%d;%dH%s" % (y, x, t))
    print(Style.RESET_ALL)

minx=0
maxx=0
miny=0
maxy=0


cols=[]
cols.append(Fore.RED)
cols.append(Fore.BLUE)
cols.append(Fore.CYAN)
cols.append(Fore.GREEN)
cols.append(Fore.MAGENTA)
cols.append(Fore.WHITE)
cols.append(Fore.YELLOW)
cols.append(Fore.RED)
cols.append(Fore.LIGHTBLUE_EX)
cols.append(Fore.LIGHTRED_EX)
cols.append(Fore.LIGHTWHITE_EX)

def drawscreen(tails,path):
    colidx=0
    for xy in path:
        putxy(xy[0]+20,xy[1]+20,"#",cols[0])
    for xy in tails:
        knot="H"
        if colidx>=1:knot=str(colidx)
        putxy(xy[0]+20,xy[1]+20,knot,cols[colidx])
        colidx+=1


def tailfollow(hx,hy,tx,ty):
    if tx+1<hx:
        tx+=1
        ty=hy
    if tx-1>hx:
        tx-=1
        ty=hy
    if ty+1<hy:
        ty+=1
        tx=hx
    if ty-1>hy:
        ty-=1
        tx=hx
    return [tx,ty]

if __name__=="__main__":
    with open(fn,"r") as fh:
        data=fh.read()
    lines=data.split("\n")


    path=[]
    tails=[]
    for ts in range(9):
        tails.append([0,0])
    hxy=[0,0]
    move_h=0
    move_v=0
    for line in lines:
        if line.strip()!="":
            command=line.split(" ")
            if command[0]=="R":move_h=int(command[1])
            if command[0]=="L":move_h=-int(command[1])
            if command[0]=="U":move_v=-int(command[1])
            if command[0]=="D":move_v=int(command[1])
            while move_h!=0:
                if move_h<0:
                    hxy[0]-=1
                    move_h+=1
                    if minx>hxy[0]:minx=hxy[0]
                if move_h>0:
                    hxy[0]+=1
                    move_h-=1
                    if minx<hxy[0]:minx=hxy[0]
                tails[0]=tailfollow(hxy[0],hxy[1],tails[0][0],tails[0][1])
                for ts in range(1,9):
                    tails[ts]=tailfollow(tails[ts-1][0],tails[ts-1][1],tails[ts][0],tails[ts][1])
                path.append((tails[8]))
                os.system("clear")
                drawscreen([hxy]+tails,path)
                time.sleep(0.1)

            while move_v!=0:
                if move_v<0:
                    hxy[1]-=1
                    move_v+=1
                    if maxy<hxy[1]:maxy=hxy[1]
                if move_v>0:
                    hxy[1]+=1
                    move_v-=1
                    if maxy>hxy[1]:maxy=hxy[1]
                tails[0]=tailfollow(hxy[0],hxy[1],tails[0][0],tails[0][1])
                for ts in range(1,9):
                    tails[ts]=tailfollow(tails[ts-1][0],tails[ts-1][1],tails[ts][0],tails[ts][1])
                path.append((tails[8]))
                os.system("clear")
                drawscreen([hxy]+tails,path)
                time.sleep(0.1)

    print(len(set(path)))
    print("{} {} {} {}".format(minx, maxx, miny, maxy))

