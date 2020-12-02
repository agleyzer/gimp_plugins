#!/usr/bin/env python
from gimpfu import *

def docprep(cimage, clayer):
   pdb.gimp_image_convert_grayscale(cimage)
   worklayer = clayer.copy()
   worklayer.name = "blur"
   worklayer.mode = DIVIDE_MODE
   cimage.add_layer(worklayer)
   pdb.plug_in_gauss(cimage, worklayer, 50, 50, 0)
   cimage.flatten()

register(
   "python_fu_docprep",
   "Clean up a photo of a B&W doc for printing",
   "Clean up a photo of a B&W doc for printing",
   "Alex Gleyzer",
   "Alex Gleyzer",
   "2020",
   "<Image>/Gleyzer/Clean up Document",
   "RGB*",
   [],
   [],
   docprep)

main()
