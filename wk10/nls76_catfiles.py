from sys import argv

if len(argv) < 3:
    exit("error -- must supply at least one input file and an output file")

out_file = open(argv[-1], "w")  #overwrite output file if it exists

for currFile in argv[1:-1]:
    
    f = open(currFile)        #open input file
    out_file.write(f.read())  #append contents of current file to outFile
    f.close()                 #close current file

print "\nFiles written to {}".format(argv[-1]) 
