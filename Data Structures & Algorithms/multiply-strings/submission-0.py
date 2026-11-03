class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        total1 = 0
        for i, c in enumerate(num1):
            if c == "0":
                total1 += 10**(len(num1)-i - 1) * 0 
            elif c == "1":
                total1 += 10**(len(num1)-i - 1) * 1
            elif c == "2":
                total1 += 10**(len(num1)-i - 1) * 2 
            elif c == "3":
                total1 += 10**(len(num1)-i - 1) * 3 
            elif c == "4":
                total1 += 10**(len(num1)-i - 1) * 4 
            elif c == "5":
                total1 += 10**(len(num1)-i - 1) * 5 
            elif c == "6":
                total1 += 10**(len(num1)-i - 1) * 6 
            elif c == "7":
                total1 += 10**(len(num1)-i - 1) * 7 
            elif c == "8":
                total1 += 10**(len(num1)-i - 1) * 8 
            elif c == "9":
                total1 += 10**(len(num1)-i - 1) * 9 

        total2 = 0
        for i, c in enumerate(num2):
            if c == "0":
                total2 += 10**(len(num2)-i - 1) * 0 
            elif c == "1":
                total2 += 10**(len(num2)-i - 1) * 1
            elif c == "2":
                total2 += 10**(len(num2)-i - 1) * 2 
            elif c == "3":
                total2 += 10**(len(num2)-i - 1) * 3 
            elif c == "4":
                total2 += 10**(len(num2)-i - 1) * 4 
            elif c == "5":
                total2 += 10**(len(num2)-i - 1) * 5 
            elif c == "6":
                total2 += 10**(len(num2)-i - 1) * 6 
            elif c == "7":
                total2 += 10**(len(num2)-i - 1) * 7 
            elif c == "8":
                total2 += 10**(len(num2)-i - 1) * 8 
            elif c == "9":
                total2 += 10**(len(num2)-i - 1) * 9 
            
        return str(total2 * total1)
