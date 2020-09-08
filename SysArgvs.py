import sys
def getnumbers(argvs):
    print("参数个数：%d"%(len(argvs)))
def showargvs(argvs):
    for i,argv in zip(range(0,len(argvs)),argvs):
        print("sys.argv[%d]=%s"%(i,argv))
getnumbers(sys.argv)
showargvs(sys.argv)