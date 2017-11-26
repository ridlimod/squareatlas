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

if __name__=="__main__":
    seqs = ls("frames")
    for k,seq in seqs.items():
        out = seq.basename + "_tile" + seq.ext
        print "tiling", k, " to",out
        tile(seq, out)
