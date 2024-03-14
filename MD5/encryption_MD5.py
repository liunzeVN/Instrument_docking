import hashlib

def md5_encrypt(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

input_data = input("请输入需要转换的字符串：")
md5_result = md5_encrypt(input_data)
print(f"MD5 Hash of '{input_data}': {md5_result}")