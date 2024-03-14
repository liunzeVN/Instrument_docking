class Solution:
    def intToRoman(self, num: int) -> str:
        # 描述所有罗马数字，包括4，9 每次都 从大的数开始
        N = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''  # 输出结果
        for i in range(len(n)):  # 遍历n的所有元素
            if num >= n[i]:      # 说明可以拿到这个罗马字符
                count = num // n[i]     # 判断能拿到几个当前罗马字符
                num -= n[i] * count     # 输入数据对应减小数值
                result += N[i] * count  # 结果累加自己能得到的罗马字符

        return result


class Solution:
    print(Solution().intToRoman(1345))