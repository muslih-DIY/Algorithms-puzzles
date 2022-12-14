from enum import IntEnum

class Roman(IntEnum):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

class Solution:
    def convert(s:str):
        length = len(s)
        value = i = letter_val = 0

        while i<length:
            letter_prev = letter_val
            letter_val = Roman[s[i]].value
            value +=letter_val
            if letter_prev < letter_val:
                value-= 2*letter_prev
            i +=1
        return value

def main():
    from testdata import ROAMANDATA_SET

    for integer,roman in ROAMANDATA_SET.items():
        finded = romantoint.convert2(roman)
        print(integer,':',roman,": converted",finded,'compare :',integer==finded)

if __name__=='__main__':
    main()
    #print(romantoint.convert('MMMMCMXCIX'))

