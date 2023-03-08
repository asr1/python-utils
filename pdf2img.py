#This takes in one pdf and splits every page into a new image.
from wand.image import Image

with(Image(filename="output.pdf", resolution=120)) as source: 
    images = source.sequence
    pages = len(images)
    for i in range(pages):
        n = i + 1
        newfilename = 'output' + str(n) + '.png'
        Image(images[i]).save(filename=newfilename)