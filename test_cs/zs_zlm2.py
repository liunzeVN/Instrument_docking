class Solution:
    THOUSANDS = ["", "M", "MM", "MMM"]
    HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    def intToRoman(self, num: int) -> str:
        return self.THOUSANDS[num // 1000] + self.HUNDREDS[(num % 1000) // 100] \
               + self.TENS[(num % 100) // 10] + self.ONES[num % 10]
        # 每次确定最左边的符号
        # roma_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        # ans = ""
        # while num!=0:
        #   signal = min([(num-roma_dict[sign],sign) for sign in roma_dict.keys() if num-roma_dict[sign]>=0])
        #   # print(signal)
        #   ans+=signal[1]
        #   num-=roma_dict[signal[1]]
        # return ans

        # 确定每位数上的值，并选择对应的符号加入

class Solution:
    print(Solution().intToRoman(340))