class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def add_to_digit(digit, carry):
            total = digit + carry
            if total%10 == total:
                return [total,0]
            elif total%100 == total:
                return [total%10, int(total/10)]
            else:
                print("error")
        carry = 1
        for idx in range(len(digits)-1,-1,-1):
            digit = digits[idx]
            new_digit, carry = add_to_digit(digit, carry)
            digits[idx] = new_digit
            if carry == 0:
                break
        if carry != 0:
            digits.insert(0,carry)
        return digits