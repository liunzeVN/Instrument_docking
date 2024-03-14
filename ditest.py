from typing import List


def convertTemperature(celsius: float) -> List[float]:
    return [celsius + 273.15, celsius * 1.80 + 32.00]


class Solution:
    celsius = 36.50
    print(convertTemperature(celsius))

print('hallor world')

#1  注释

'''一行注释
二行注释'''


"""双引号多行注释"""

print("answer")
print("true")
print("false")


