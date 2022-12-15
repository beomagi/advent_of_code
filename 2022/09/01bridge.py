#!/usr/bin/env python3

import sys

fn=sys.argv[1]

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
    txy=[0,0]
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
                if move_h>0:
                    hxy[0]+=1
                    move_h-=1
                txy=tailfollow(hxy[0],hxy[1],txy[0],txy[1])
                path.append(str(txy))

            while move_v!=0:
                if move_v<0:
                    hxy[1]-=1
                    move_v+=1
                if move_v>0:
                    hxy[1]+=1
                    move_v-=1
                txy=tailfollow(hxy[0],hxy[1],txy[0],txy[1])
                path.append(str(txy))

    print(len(set(path)))


