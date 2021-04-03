import os
from PIL import Image

wd = os.path.realpath(__file__)[0:len(os.path.realpath(__file__))-9]

pic = None

def registerManually():
    global pic
    print("No image found in default image location. Please input image path:")
    pic = input()

if os.path.exists(os.path.join(wd,"image")):
    if len(os.listdir(os.path.join(wd,"image"))) > 0:
        if len(os.listdir(os.path.join(wd,"image"))) > 1:
            print("Warning! More than 1 Image detected. The program will work with the follwoing image:")
            print(os.listdir(os.path.join(wd,"image"))[0])
        pic = os.path.join(os.path.join("image",os.listdir(os.path.join(wd,"image"))[0]))
    else:
        registerManually()
else:
    registerManually()

f = open("output.html","w")
f.write("<head></head><body>")     

if os.path.isfile(pic):
    im = Image.open(pic)
    f.write('<table style="border-collapse:collapse;width:'+str(im.size[0])+'px;height:'+str(im.size[1])+'px;">')
    px = im.load()
    hheight = "%.3f" % ((1/im.size[1])*100)
    wwidth = "%.3f" % ((1/im.size[0])*100)
    
    for y in range(im.size[1]):
        f.write('<tr style="border-collapse:collapse;">')
        for x in range(im.size[0]):
            f.write('<td style="border-collapse:collapse;width:'+wwidth+'%;height:'+hheight+'%;background-color:rgb'+str(px[x,y])+'"></td>')
        f.write("</tr>")
    f.write("</table>")
else:
    f.write("<h1>pic.png/.jpg/.jpeg does NOT exist</h1>")

f.write("</body>")
f.close()
print("done.")