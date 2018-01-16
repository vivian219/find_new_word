def remove_space(sourceFileName,destFileName):
    fs=open(sourceFileName)
    fd=open(destFileName,'w')
    for line in fs:
        new_line=line.replace(" ","",20)
        fd.write(new_line)
    fs.close()
    fd.close()
remove_space("term.txt","term.merge.txt")