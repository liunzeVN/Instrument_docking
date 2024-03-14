from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    n = len(strs) # 记录字符串的数量
    min = len(strs[0]) # 记录最小的字符串长度
    min_str = strs[0] # 记录最小的字符串
# 寻找最短的字符串
    for i,x in enumerate(strs):
        y = len(x)
        if y<min:
            min = y
            min_str = x
# 从min长度开始比较，依次减小，第一次成功的即为最长前缀
    for i in range(min,0,-1):
        k = 1
        for j in range(0,n):
            if min_str[0:i]!=strs[j][0:i]:
                k =0
                break
        if k==1:
            return min_str[0:i]

    return ""


def main():
    s = ["flower","flow","flight"]
    a = ["cardog","caracecal","car"]

    print(longestCommonPrefix(a))
    print(longestCommonPrefix(s))

if __name__ == "__main__":
    main()