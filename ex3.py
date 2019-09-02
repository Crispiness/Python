import sys

#args =sys.argv[1:] # 리스트 형태로

#for i in args:
#    print (i)

f =  open(sys.argv[1], "r")
g =  open(sys.argv[2], "w")

for line in f :
    g.write(line)

g.close()
f.close()
