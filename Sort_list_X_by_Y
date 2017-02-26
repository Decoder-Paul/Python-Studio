'''
In the sample input, T = 1 and N = 4, where N is the number of days.

Tasks provided to Monk A on first day is 3 and binary representation of 3 is { 11 }2, which contains 2 ones.

Tasks provided to Monk A on second day is 4 and binary representation of 4 is { 100 }2, which contains 1 ones.

Tasks provided to Monk A on third day is 7 and binary representation of 7 is { 111 }2, which contains 3 ones.

Tasks provided to Monk A on fourth day is 10 and binary representation of 10 is { 1010 }2, which contains 2 ones.

So the Output will be: 4 3 10 7
'''
for _ in xrange(input()):
    n = int(raw_input())
    arr = map(int, raw_input().split())
    l=[bin(i)[2:].count('1') for i in arr]
    data = [x for (y,x) in sorted(zip(l,arr), key=lambda pair: pair[0])]
#    X = [x for (y,x) in sorted(zip(l,arr))]
    print ' '.join(map(str,data))