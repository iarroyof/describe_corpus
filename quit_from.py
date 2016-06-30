file_i = 
file_s
file_o

with open(file_i) as fi, open(file_s) as fs:
    indexes = [s for i, line_i in enumerate(fi) for s, line_s in enumerate(fs) if line_i == line_s]
    
with open(file_o, "w") as fo, open(file_s) as fs:
    lines_o = [line for i, line in enumerate(fs) if i not in indexes]
    for line in lines_o:
        fo.write(line)
