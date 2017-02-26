# from collections import defaultDict
for t in xrange(input()):
    n = input()
    arr = raw_input().split()

    d = {}   #empty dict
    print arr
    for a in arr:
        if not a in d:
            d[a] = 0
        else:
            del d[a]
    # print d
    if len(d) >= 1:
        for k in d:
            print k
    else:
        print -1