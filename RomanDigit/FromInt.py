class Solution:
    symbol = ('I', 'V', 'X', 'L', 'C', 'D','M')
    def intToRoman(self, num: int) -> str:
        i=0
        roman =''
        while 1:
            d = num%10
            num = int(num/10)
            roman = self.findpattern(d,i)+roman
            if num==0:return roman
            i+=2
    def findpattern(self,digit:int,position:int) -> str:
        if digit == 0 :return ''
        s1 = self.symbol[position]
        if digit<4:return s1*digit
        s2 = self.symbol[position+1]
        if digit==4:return s1+s2
        if digit<9:return s2+s1*(digit-5)
        s3 = self.symbol[position+2]
        return s1+s3