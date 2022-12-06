#!/usr/bin/env python3


if __name__=="__main__":
    with open("./input.txt","r") as fh:
        lines=fh.read()

    linesep=lines.strip().split("\n")

    d_my_rps={
            "X":{"p":1,"A":3,"B":0,"C":6},
            "Y":{"p":2,"A":6,"B":3,"C":0},
            "Z":{"p":3,"A":0,"B":6,"C":3}
        }



    points=0
    for aline in linesep:
        play=aline.split(" ")
        opp=play[0]
        myp=play[1]
        pickpoints=d_my_rps[myp]["p"]
        winpoints=d_my_rps[myp][opp]
        points+=pickpoints+winpoints
    print(points)




