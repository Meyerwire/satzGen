from random import randint

def GenSent(wList,tkm):
    tkm.showinfo("Satz",wList['Namen'][str(randint(0,len(wList['Namen'])))])