import os
from PIL import Image

f = open("output.html","w")
f.write("<head></head><body>")

if os.path.isfile("pic.png"):
    pic = "pic.png"
elif os.path.isfile("pic.jpg"):
    pic = "pic.jpg"
elif os.path.isfile("pic.jpeg"):
    pic = "pic.jpeg"
else:
    pic = ""        

if len(pic)>0:
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