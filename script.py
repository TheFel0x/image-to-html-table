import os, argparse
from PIL import Image

def main():

    # args stuff
    global args

    parser = argparse.ArgumentParser()
    parser.add_argument("input",type=str,help="image file")
    parser.add_argument("-o","--output",type=str,help="specify output directory")
    parser.add_argument("--overwrite",action='store_true',help="can replace existing output file")
    parser.add_argument("--name",type=str,help="name of output file")
    parser.add_argument("--type",type=str,choices=["code","website"],help="'website' puts out the file with head and body tags while 'code' only saves the table part in a file")

    args = parser.parse_args()

    in_file = args.input
    out_path = ""
    out_name = "output.html"

    if not args.output == None and os.path.isdir(args.output): # chooses working directory when chosen dir doesnt exist. that's not great
        out_path = args.output
    else:
        out_path = os.getcwd()

    do_overwrite = args.overwrite

    if not args.name == None:
        out_name = args.name

    if args.type == "code":
        is_full_html = False
    else:
        is_full_html = True

    out_file = os.path.join(out_path,out_name)

    # file stuff
    im = None

    if os.path.exists(in_file):
        try:
            im = Image.open(in_file)
        except:
            print("Unable to load image file.")
    else:
        print("File "+in_file+" not found.")

    # table building

    if do_overwrite and os.path.isfile(out_file):
        os.remove(out_file)

    f = open(out_file,"w")
    
    # build file

    if is_full_html:
        f.write("<head></head><body>")     

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
    
    if is_full_html:
        f.write("</body>")
    f.close()
    print("Done.")

if __name__ == "__main__":
    main()