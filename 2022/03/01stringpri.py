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

    sums=0
    for aline in linesep:
        pock1=aline[:int(len(aline)/2)]
        pock2=aline[int(len(aline)/2):]
        matches=[]
        for letter in pock1:
            if letter in pock2:
                if letter not in matches:
                    matches.append(letter)
        for eachmatch in matches:
            sums+=charpri(eachmatch)
    print(sums)
