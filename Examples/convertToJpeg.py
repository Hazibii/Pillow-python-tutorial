from __futre__ import print_function
import os, sys
from PIL import image


for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f  + ".jpg"
    if infile !=outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)
            
