import sys
from math import sqrt

def bestfit(x,y,f):
    numpix=x*f*y
    pixq=sqrt(numpix)
    cs,fs = pixq//x,pixq//y
    xs,ys = cs*x,fs*y

    left = f-fs*cs
    if left == 0:
        return cs,fs
    if x>=y:
        if left <= cs:
            return cs,fs+1
        else:
            return cs+1,fs+1
    else:
        if left <= fs:
            return cs+1,fs
        else:
            return cs+1,fs+1

def block(x,y,f):
    c,f = bestfit(x,y,f)
    return (c,c*x),(f,f*y)

def indx(c,f,frame):
    return (frame-1)%c,(frame-1)//c

if __name__=="__main__":
    test = [(512,384,120),
            (1280,960,60),
            (1980,1080,120),
            (640,480,120),
            (384,720,25)]

    for (x,y,fn),((c,rx),(f,ry)) in map(lambda x : (x,block(*x)),test):
        print x,y,fn,':',c,rx,f,ry,c*f

    print "\n"
    rx,ry,nf = 285,140,167
    (c,x),(f,y) = block(rx,ry,nf)
    print rx,ry,nf,":",c,x,f,y,c*f
    for (x,y),f in map(lambda x:(indx(c,f,x),x),range(1,nf+1)):
        print f,":",x,y
