#!/usr/bin/env python3

def charpri(achar):
    if (achar >= "a") and (achar <= "z"):
        return 1+ord(achar)-ord("a")
    if (achar >= "A") and (achar <= "Z"):
        return 27+ord(achar)-ord("A")
    return 0

if __name__=="__main__":
    with open("./input.txt","r") as fh:
        lines=fh.read()

    linesep=lines.strip().split("\n")

    idx=0
    sums=0
    while idx<len(linesep):
        line1=linesep[idx]
        line2=linesep[idx+1]
        line3=linesep[idx+2]
        idx+=3
        for chars in line1:
            if chars in line2:
                if chars in line3:
                    sums+=charpri(chars)
                    #print("{} {}".format(idx, sums))
                    break
    print(sums)
