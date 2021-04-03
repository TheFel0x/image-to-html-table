import os, argparse
from PIL import Image

def main():

    # args stuff
    global args

    parser = argparse.ArgumentParser()
    parser.add_argument("input",type=str,help="image file")
    parser.add_argument("-o","--output",type=str,help="specify output directory")
    parser.add_argument("-n","--name",type=str,help="name of output file (default name is 'output.html')")
    parser.add_argument("-t","--type",type=str,choices=["code","website"],help="'website' puts out the file with head and body tags while 'code' only saves the table part in a file")
    #parser.add_argument("--ratio",type=str,choices=["fixed","window"],help="'fixed' forces original aspect ratio while 'window' is affected by the window aspect ratio")
    parser.add_argument("-b","--border",action='store_true',help="turns on border")
    parser.add_argument("--nocollapse",action='store_true',help="disables border collapse")
    parser.add_argument("--overwrite",action='store_true',help="can replace existing output file")
    parser.add_argument("-r","--resize",type=int,help="resizes image. value is new width in pixel. --> changes amounnt of pixels")
    parser.add_argument("-s","--size",type=int,help="width of the resulting table in pixel --> changes size of table")

    args = parser.parse_args()

    in_file = args.input
    
    out_path = args.output if not args.output == None else os.getcwd()
    do_overwrite = args.overwrite
    out_name = args.name if not args.name == None else "output.html"
    is_full_html = True if args.type == "code" else False
    out_file = os.path.join(out_path,out_name)

    new_width = args.resize if not args.resize == None else -1 

    style_border = "border: 1px solid black;" if args.border else ""
    style_collapse = "border-collapse: none;" if args.nocollapse else "border-collapse: collapse;"

    im = Image.open(in_file)

    # table building

    if do_overwrite and os.path.isfile(out_file):
        os.remove(out_file)

    f = open(out_file,"w")
    
    # build file

    if is_full_html:
        f.write("<head></head><body>")     

    style = style_border+style_collapse

    # if args.ratio == "fixed" or args.ratio == None:
    #     f.write('<table style="'+style+'width:'+str(im.size[0])+'px;height:'+str(im.size[1])+'px;">')
    # else:
    #     f.write('<table style="'+style+'">')
    
    f.write('<table style="'+style+'width:'+str(im.size[0])+'px;height:'+str(im.size[1])+'px;">')

    px = im.load()
    hheight = "%.3f" % ((1/im.size[1])*100)
    wwidth = "%.3f" % ((1/im.size[0])*100)
        
    for y in range(im.size[1]):
        f.write('<tr style="border-collapse:collapse;">')
        for x in range(im.size[0]):
            f.write('<td style="border-collapse:collapse;width:'+wwidth+'%;height:'+hheight+'%;background-color:rgb'+str(px[x,y])+'"></td>')
        f.write("</tr>")
    f.write("</table>")
    
    if is_full_html:
        f.write("</body>")
    f.close()
    print("Done.")

if __name__ == "__main__":
    main()