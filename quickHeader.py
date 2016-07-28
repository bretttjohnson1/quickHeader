import re
import getopt
import sys
import os

#^(?!")(?!])(unsigned|void|char|int|char|long)(((?!main).)*)\)

arguments = None
remain =None
try:
    arguments, remain  = getopt.getopt(sys.argv[1:],"i:o:")
except:
    print ("script only accepts arguments of -i for input file and -o for output file")
    quit()

inputfilename=None
outputfilename=None
for opt,arg in arguments:
    if opt =='-i':
        inputfilename = arg
    elif opt == '-o':
        outputfilename = arg
inputfile = None
outputfile = None
try:
    inputfile=open(inputfilename,'r')
except:
    print("Inputfile does not exist")
    quit()

try:
    outputfile = open(outputfilename,'w+')

except:
    print ("Outputfilename not valid")
    quit()

reg = re.compile("""^(?!")(?!')(?!])(unsigned|void|int|char|long|double|float|short)(((?!main).)*)\)""")

methodlist = []
for line in inputfile:
    for match in re.finditer(reg,line):
        methodlist.append(match.group(0))
outputfile.write("#ifndef "+os.path.basename(outputfile.name).split('.')[0]+"_header_file"+"\n")
outputfile.write("#define "+os.path.basename(outputfile.name).split('.')[0]+"_header_file"+"\n\n")
for method in methodlist:
    outputfile.write(method+";"+"\n\n")
outputfile.write("#endif")
