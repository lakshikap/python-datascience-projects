f = open("File_Handle text", "r")
# for line in f:
#    print(line)

lines = f.readlines()
print(lines)

f.close()



