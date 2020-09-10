import sys,argparse
def sequentialsearch(alist,item):#in
    pos=0
    found=False
    while pos<len(alist) and not found:
        if alist[pos]==item:
            found=True
        else:
            pos+=1
    return found

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--list',type=str,help="列表元素；使用逗号将列表元素隔开")
    parser.add_argument('--key')
    args=parser.parse_args()
    a=args.list.split(',')
    if sequentialsearch(a,args.key):
        print('found')
    else:
        print('not found')
