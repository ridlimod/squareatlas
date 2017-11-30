from FileSequence.FileSequence import ls
from wand.image import Image
from bestfit import block, indx
import os

def tile( seq, ofilename ):
    refImage = Image(filename=os.path.join(seq.path,seq.printpatt.format(seq.first)))
    rx = refImage.width
    ry = refImage.height
    count = seq.last-seq.first+1
    (bx,x),(by,y) = block(rx,ry,count)
    refImage.close()

    imgContainer=Image(width=x,height=y)
    for i in range(seq.first,seq.last+1):
        filename = os.path.join(seq.path,seq.printpatt.format(i))
        with Image(filename=filename) as tile:
            cx,cy=indx(bx,by,i)
            left=cx*rx
            top=cy*ry
            imgContainer.composite(image=tile,left=left,top=top)
    imgContainer.save(filename=ofilename)
    imgContainer.close()

    return bx,by,count

if __name__=="__main__":
    seqs = ls("frames")
    for k,seq in seqs.items():
        out = seq.basename + "_tile" + seq.ext
        print "tiling", k, " to",out
        c,f,n = tile(seq, out)
        nout = seq.basename + "_tile-{0}X{1}X{2}_".format(c,f,n) + seq.ext
        os.rename(out,nout)
        print "La imagen tiene {0}X{1} cells y contiene {2} frames".format(c,f,n)
