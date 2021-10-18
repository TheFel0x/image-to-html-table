import os, argparse, sys
from PIL import Image

def main():

    # TODO: remove after interactive input finished
    # parser = argparse.ArgumentParser()
    # parser.add_argument("input",type=str,help="image file")
    # parser.add_argument("-o","--output",type=str,help="specify output directory")
    # parser.add_argument("-n","--name",type=str,help="name of output file (default name is 'output.html')")
    # parser.add_argument("-t","--type",type=str,choices=["code","website"],help="'website' puts out the file with head and body tags while 'code' only saves the table part in a file")
    # parser.add_argument("-b","--border",action='store_true',help="turns on border")
    # parser.add_argument("--nocollapse",action='store_true',help="disables border collapse")
    # parser.add_argument("-v","--overwrite",action='store_true',help="can replace existing output file")
    # parser.add_argument("-r","--resize",type=int,help="resizes image. value is new width in pixel. --> changes amounnt of pixels")
    # parser.add_argument("-s","--size",type=int,help="width of the resulting table in pixel --> changes size of table")

    # args = parser.parse_args()

    print("Enter path of the input image.")
    in_file = input("path: ")
    # in_file = args.input

    # print("Where do you want to output the file?\nEnter full directory or leave empty to save in working directory.")
    # inp = input("path: ")
    # if inp == None:
        # out_path = os.getcwd()
    # else:
        # out_path = inp
    # out_path = args.output if not args.output == None else os.getcwd()
    # FIXME: this doesnt work. remove the line below this one and make code above work
    out_path = os.getcwd()

    print("Overwrite the existing file if necessary? (y/N)")
    inp = input("y/N: ")
    inp = "n" if inp == None else inp
    if inp.lower() == "y" or inp.lower() == "yes":
        do_overwrite = True
    else:
        do_overwrite = False
    #do_overwrite = args.overwrite
    
    # print("What name should the output have? (leave blank for \"output.html\")")
    # inp = input("filename: ")
    # if inp == None:
    #     out_name =  "output.html"
    # else:
    #     out_name = inp
    #out_name = args.name if not args.name == None else "output.html"
    # FIXME: this doesnt work. remove the line below this one and make code above work
    out_name = "output.html"

    print("Do you want the other HTML tags to be automatically added? (Working HTML page) (Y/n)")
    inp = input("Y/n: ")
    inp = "y" if inp == None else inp
    if inp.lower() == "n" or inp.lower() == "no":
        is_full_html = False
    else:
        is_full_html = True
    #is_full_html = True if args.type == "code" else False

    print("Note: your file will be saved as:")
    out_file = os.path.join(out_path,out_name)
    print(out_file) 

    print("Want a border around your table cells (pixels)? (y/N)")
    inp = input("y/N: ")
    inp = "n" if inp == None else inp
    if inp.lower() == "y" or inp.lower() == "yes":
        border = True
    else:
        border = False

    style_border = "border: 1px solid black;" if border else ""

    print("Prevent borders (if enabled) from collapsing? (y/N)")
    inp = input("y/N: ")
    if inp.lower() == "y" or inp.lower() == "yes":
        nocollapse = True
    else:
        nocollapse = False

    style_collapse = "border-collapse: none;" if nocollapse else "border-collapse: collapse;"

    im = Image.open(in_file)

    # TODO: make resizing possible again
    # if not args.resize == None:
    #     size = (args.resize,args.resize*im.height//im.width)
    #     im = im.resize(size)

    if not do_overwrite and os.path.isfile(out_file):
        print("File exists. Terminating script. Add '--overwrite' / '-v' or change the outputs name with '--name' / '-n'")
        sys.exit()

    f = open(out_file,"w")
    
    if is_full_html:
        f.write("<head></head><body>")     

    style = style_border+style_collapse

    # TODO: make size settings possible again
    table_width = im.size[0] # if args.size == None else args.size
    table_height = im.size[1] # if args.size == None else im.size[1]*args.size//im.size[0]

    f.write('<table style="'+style+'width:'+str(table_width)+'px;height:'+str(table_height)+'px;">')

    px = im.load()
    cell_height = "%.3f" % ((1/table_height)*100)
    cell_width = "%.3f" % ((1/table_width)*100)
        
    for y in range(im.size[1]):
        f.write('<tr style="'+style+'">')
        for x in range(im.size[0]):
            f.write('<td style="'+style+';width:'+cell_width+'%;height:'+cell_height+'%;background-color:rgb'+str(px[x,y])+'"></td>')
        f.write("</tr>")
    f.write("</table>")
    
    if is_full_html:
        f.write("</body>")
    f.close()
    
    print("Done. ("+out_file+")")

if __name__ == "__main__":
    main()
