# /usr/bin/python3


# @Time  :2023/12/8 10:40
# @Author :测试员小李

import random

def greatphone():
    """生成随机手机号"""

    # choice方法随机抽取列表中的手机号码段
    str_start = random.choice(['135','138','186'])
    # sample方法，列表中随机抽取8个尾数
    str_end = ''.join(random.sample('0123456789',8))
    phone = str_start + str_end
    # 返回的手机号用于传给api检验
    return phone