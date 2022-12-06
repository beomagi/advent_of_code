#!/usr/bin/env python3


if __name__=="__main__":
    with open("./input.txt","r") as fh:
        lines=fh.read()

    linesep=lines.strip().split("\n")

    d_my_rps={
            "X":{"p":0,"A":3,"B":1,"C":2},
            "Y":{"p":3,"A":1,"B":2,"C":3},
            "Z":{"p":6,"A":2,"B":3,"C":1}
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




