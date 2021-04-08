# Image to HTML table
 Turns image into an HTML table.

Basically [this](https://gist.github.com/TheFel0x/1623c8b0f56fbde4dd6152f41fc41b62), except not as a gist.

[Click here for example page](https://thefel0x.github.io/examples/table.html) ([Click here for example source](https://github.com/TheFel0x/TheFel0x.github.io/blob/master/examples/table.html))

**Warning:** Depending on your browser and device large images might not load very well. Also file sizes are not small since each individual pixel requires HTML code. That's a lot of code for large images.


## How to use:
`script.py [-h] [-o OUTPUT] [-n NAME] [-t {code,website}] [-b] [--nocollapse] [-v] [-r RESIZE] [-s SIZE] input`

### Examples:

* `script.py image.png`
* `script.py image.png -o ~/output`
* `script.py image.png -o ~/output -n image-table.html -t website -b -r 40 -s 200`


| flag | values | meaning |default| example |
|--|--|--|--|--|
| `-h` `--help` | (none) | shows help ||||
| `-o` `--output` | (string) | output location|working directory|`-o ~/output`|
|`-n` `--name`|(string)|output name|"output.html"|`-n myoutput.html`|
|`-t`|code / website|output as full website with head and body tags or only output table code|website|`-t code`|
|`-b` `--border`||turn on table border|||
|`--nocollapse`||deactivates border collapse||
|`-v` `--overwrite`||allows script to replace output file|||
|`-r` `--resize`|(integer)|resizes image. the outputs amount of pixels therefore changes. value decides new width / x pixel amount | (image width) | `-r 60`
| `-s` `--size` | (integer) | changes size of table. value represents width. meant to make small images visible | (image size) | `-s 400`

## `-h` output:
```
usage: script.py [-h] [-o OUTPUT] [-n NAME] [-t {code,website}] [-b] [--nocollapse] [-v] [-r RESIZE] [-s SIZE] input

positional arguments:
  input                 image file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        specify output directory
  -n NAME, --name NAME  name of output file (default name is 'output.html')
  -t {code,website}, --type {code,website}
                        'website' puts out the file with head and body tags while 'code' only saves the table part in a file
  -b, --border          turns on border
  --nocollapse          disables border collapse
  -v, --overwrite       can replace existing output file
  -r RESIZE, --resize RESIZE
                        resizes image. value is new width in pixel. --> changes amounnt of pixels
  -s SIZE, --size SIZE  width of the resulting table in pixel --> changes size of table
```
