#lookup table for prime no. ASCII alphabets
lookup = {
    'A':'C',
    'B':'C',
    'C':'C',
    'D':'C',
    'E':'C',
    'F':'G',
    'G':'G',
    'H':'G',
    'I':'T',
    'J':'I',
    'K':'I',
    'L':'I',
    'M':'O',
    'N':'O',
    'O':'O',
    'P':'O',
    'Q':'O',
    'R':'S',
    'S':'S',
    'T':'S',
    'U':'S',
    'V':'S',
    'W':'Y',
    'X':'Y',
    'Y':'Y',
    'Z':'Y',
    'a':'a',
    'b':'a',
    'c':'a',
    'd':'e',
    'e':'e',
    'f':'e',
    'g':'g',
    'h':'g',
    'i':'g',
    'j':'k',
    'k':'k',
    'l':'k',
    'm':'m',
    'n':'m',
    'o':'m',
    'p':'q',
    'q':'q',
    'r':'q',
    's':'q',
    't':'q',
    'u':'q',
    'v':'q',
    'w':'q',
    'x':'q',
    'y':'q',
    'z':'q',
}
t = int(raw_input())

while t != 0:
    length = int(raw_input());
    word = raw_input();
    newWord=''
    for e in word :
        newWord += lookup[e];
    print newWord;
    t -= 1;