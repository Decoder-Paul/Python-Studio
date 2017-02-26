MOD = 100000
n = int(raw_input())
arr = map(int, raw_input().split())
print arr
for i in xrange(4):
    temp = {}
    hasnot0 = False
    for j in xrange(n):
        chunk = arr[j] / (MOD ** i) % MOD
        if chunk != 0:
            hasnot0 = True
        if chunk not in temp:
            temp[chunk] = [arr[j]]
        else:
            temp[chunk].append(arr[j])
    if hasnot0:
        arr = []
        for k in sorted(temp.keys()):
            for a in temp[k]:
                print a,
                arr.append(a)
        print
    else:
        break