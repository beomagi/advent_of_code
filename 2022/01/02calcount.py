#!/usr/bin/env python3
if __name__=="__main__":
    with open("./input.txt","r") as fh:
        lines=fh.read()

    linesep=lines.split("\n")

    most=[0,0,0]
    currentcal=0
    for aline in linesep:
        if len(aline)>=1:
            currentcal+=int(aline)
            if currentcal>most[0]:
                most[0]=currentcal
        else:
            most.sort()
            currentcal=0
    print(most[0]+most[1]+most[2])



