def romanToInt(s) -> int:
    Roman2su = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    n = len(s)

    for index in range(n - 1):
        value = Roman2su[s[index]]

        if index < n-1 and value < Roman2su[s[index + 1]]:
            result -= value

        else:
            result += value

    result += Roman2su[s[-1]]

    return result
    #     if Roman2su[s[index]] < Roman2su[s[index + 1]]:
    #         result -= Roman2su[s[index]]
    #     else:
    #         result += Roman2su[s[index]]
    #
    # return result + Roman2su[s[-1]]


def main():
    s = input("请输入罗马数字")

    print(romanToInt(s))

if __name__ == "__main__":
    main()