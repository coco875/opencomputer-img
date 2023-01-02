import image_slicer
from tkinter import filedialog
 
fname = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("image","*.png, *.jpg"),("all files","*.*")))
print("Input the number of row that must be equal to the number of column")
rows = int(input("how many rows? > "))
 
image_slicer.slice(fname, number_tiles=rows)
print("done")