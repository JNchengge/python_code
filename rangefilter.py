import sys
low=sys.argv[1]
high=sys.argv[2]
for line in sys.stdin:
    value=int(line)
    if value>=low and value<=high:
        print(str(value))
