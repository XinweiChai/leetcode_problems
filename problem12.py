class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        symb_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                     5: 'V', 4: 'IV', 1: 'I'}
        for i in symb_dict.keys():
            while num >= i:
                num -= i
                roman += symb_dict[i]
        return roman


print(Solution().intToRoman(3999))
