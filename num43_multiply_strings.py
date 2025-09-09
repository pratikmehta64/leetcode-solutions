class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        interim_lines = []
        for idx, num2_digit in enumerate(num2[::-1]):
            carry = 0
            line_main = ''.join(["0" for _ in range(idx)])
            
            for num1_digit in num1[::-1]:
                prod = int(num2_digit) * int(num1_digit)
                main = (prod + carry)%10
                line_main = str(main) + line_main
                carry = int(''.join(str((prod + carry) / 10).split('.')[0]))
           
            if carry:
                line_main = str(carry) + line_main
            
            interim_lines.append(line_main)
        product = sum([int(line) for line in interim_lines])
        return str(product)
            