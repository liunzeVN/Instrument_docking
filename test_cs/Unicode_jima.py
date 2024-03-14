import unicodedata

#失败实验
byte_string = b'\xa5\x04\x11"' \
              b'"\x80!h\x89\x98\r\x00\x1a=\x1f\xb4\xe6A' \
              b'`\x00\x00\x02>\xb333>L\xcc\xcd=\xcc\xcc\xcd\x00\x00\x1e\xb6\x12'
print(byte_string)
print(unicodedata.normalize('NFD',byte_string))
print(unicodedata.normalize('NFKD',byte_string))
print(unicodedata.normalize('NFKC',byte_string))

# t1 = unicodedata.normalize('NFC',byte_string)
# print(byte_string)
# t2 = unicodedata.normalize('NFD',byte_string)
# print(byte_string)

# Unicode_string = byte_string.decode("unicode_escape") # 解码为文本
# #Unicode_string = byte_string.decode("utf-8") # 解码为utf-8
# #Unicode_string = byte_string.decode("utf-16") # 解码为utf-16
# #Unicode_string = byte_string.decode("utf-32") # 解码为utf-32
# #Unicode_string = byte_string.decode("gbk") # 解码为gbk
# print(Unicode_string)