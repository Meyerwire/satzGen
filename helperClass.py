from random import randint

def GenSent(wList,tkm):
    satz = ""
    for val in wList:
        satz += wList[val][str(randint(1,len(wList[val])))]
        satz +=" "
    satz.strip
    satz+="."
    tkm.showinfo("Satz",satz)

def AddWord():
    print("test")