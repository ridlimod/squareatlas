import sys
from math import sqrt,ceil

def bestfit(x,y,f):
    numpix=x*f*y
    pixq=sqrt(numpix)
    cs,fs = pixq//x,pixq//y
    xs,ys = cs*x,fs*y

    pixq=ceil(pixq)

    left = f-fs*cs

    cs = int(cs)
    fs = int(fs)
    if left == 0:
        return cs,fs
    # print x,pixq,xs,abs(pixq-(xs+x))
    # print y,pixq,ys,abs(pixq-(ys+y))
    if abs(pixq-(xs+x)) > abs(pixq-(ys+y)):
        if left <= cs:
            return cs,fs+1
        elif left <= fs:
            return cs+1,fs
        else:
            return cs+1,fs+1
    else:
        if left <= fs:
            return cs+1,fs
        elif left <= cs:
            return cs,fs+1
        else:
            return cs+1,fs+1

def block(x,y,f):
    c,f = bestfit(x,y,f)
    return (c,int(c*x)),(f,int(f*y))

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

    print "\n"
    rx,ry,nf = 1280,720,40
    (c,x),(f,y) = block(rx,ry,nf)
    print rx,ry,nf,":",c,x,f,y,c*f
    for (x,y),f in map(lambda x:(indx(c,f,x),x),range(1,nf+1)):
        print f,":",x,y
