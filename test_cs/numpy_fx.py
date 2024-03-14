import numpy as np

def npsum():
    # a = [0, 1, 2, 3, 4]
    # b = [5, 6, 7, 8, 9]
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([5, 6, 7, 8, 9])

    # for i in range(len(a)):
    #     c.append(a[i]**2 + b[i]**3)
    c = a**2 + b**3  #使用numpy模块后的科学计算，不需要使用循环

    return c

# print((pysum()))
print(npsum())

