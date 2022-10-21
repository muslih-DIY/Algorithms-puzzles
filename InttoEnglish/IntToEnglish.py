class Solution:
    basewords = (
        'One',  'Two' ,'Three' , 'Four' ,'Five',  'Six', 'Seven' ,'Eight',
         'Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen',
         'Sixteen','Seventeen','Eighteen','Nineteen') 
    tyword =('Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety')
    trypack = ('Thousand','Million')
    def numberToWords(self, num: int) -> str:
        if num == 0 :return 'Zero'
        return self.Word(num)
        
    
    def Word(self,number):
        if number==0:return ''
        if number <=len(self.basewords):return self.basewords[number-1]
        if number <100 :return ' '.join([self.tyword[number//10-2],self.Word(number%10)]).rstrip()
        if number <1000:return ' '.join([self.basewords[number//100-1],'Hundred',self.Word(number%100)]).rstrip()
        if number<1000000:return ' '.join([self.Word(number//1000),'Thousand',self.Word(number%1000)]).rstrip()
        if number<1000000000:return ' '.join([self.Word(number//1000000),'Million',self.Word(number%1000000)]).rstrip()
        if number<1000000000000:return ' '.join([self.Word(number//1000000000),'Billion',self.Word(number%1000000000)]).rstrip()
        return ' '.join([self.Word(number//1000000000000),'Trillion',self.Word(number%1000000000000)]).rstrip()