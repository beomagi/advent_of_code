#!/usr/bin/env python3

import sys

fn=sys.argv[1]


def fillfiles(commandlist):
    files={}
    curdir="/"
    for cmd in commandlist:
        if cmd.strip()!="":
            if cmd.startswith("$"):
                commparam=cmd.split(" ")
                if commparam[1]=="cd":
                    if commparam[2]=="/": #explicit home
                        curdir="/"
                    elif commparam[2]=="..": #up one
                        curdir="/".join(curdir.split("/")[:-1])
                    else:
                        curdir=curdir+"/"+commparam[2] #in one
                    curdir=curdir.replace("//","/") #special condition of home
                if curdir not in files:
                    files[curdir]={"f":[]}
            elif cmd.startswith("dir"):
                adir={}
                adir["dir"]=(curdir+"/"+cmd.split(" ")[1]).replace("//","/")
                files[curdir]["f"].append(adir)
            else:
                fileinfo=cmd.split(" ")
                afile={}
                afile["file"]=fileinfo[1]
                afile["size"]=fileinfo[0]
                files[curdir]["f"].append(afile)
    return files


def sizecalc(ftree,adir):
    size=0
    for eachentry in ftree[adir]["f"]:
        if "size" in eachentry:
            size+=int(eachentry["size"])
        else:
            sizecalc(ftree,eachentry["dir"])
            eachentry["size"]=int(ftree[eachentry["dir"]]["size"])
            size+=int(ftree[eachentry["dir"]]["size"])
    ftree[adir]["size"]=size
        







if __name__=="__main__":
    with open(fn,"r") as fh:
        data=fh.read()
    lines=data.split("\n")

    tree=fillfiles(lines) #parse and populate tree
    sizecalc(tree,"/")    #add size information to dirs

    
    sumsize=0
    for dirs in tree:
        size=tree[dirs].get("size",0)
        if size < 100000:
            sumsize+=size
    print(sumsize)

