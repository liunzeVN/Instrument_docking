from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    res = 1256
    a = res // 10
    b = a // 10
    c = b // 10

    a_mo = res % 10
    b_mo = a % 10
    c_mo = b % 10
    d_mo = c % 10

    a_mo_test = res % a_mo
    b_mo_test = res % b_mo
    c_mo_test = res % c_mo
    d_mo_test = res % d_mo

    for i in range(0, 6, 2):
        print(i, end="")

    print('\n')
    print(res)
    print(a)
    print(b)
    print(c)
    print('\n')
    print(a_mo)
    print(b_mo)
    print(c_mo)
    print(d_mo)
    print('\n')
    print(a_mo_test)
    print(b_mo_test)
    print(c_mo_test)
    print(d_mo_test)
