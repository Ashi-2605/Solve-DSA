class Solution:
    def myAtoi(self, s) :
        i = 0
        n = len(s)

        # 1. Leading spaces skip karo
        while i < n and s[i] == ' ':
            i += 1

        # 2. Sign check karo
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # 3. Digits read karo
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. Overflow check
            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31

            num = num * 10 + digit
            i += 1

        return sign * num
        