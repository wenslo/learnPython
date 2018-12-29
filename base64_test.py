import base64

print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

print(base64.b64encode(b'abcd'))
print(base64.b64decode(b'YWJjZA=='))


def safe_base64_decode(s):
    blen = len(s) % 4
    if blen != 0:
        for x in range(0, blen):
            s = s + b'='

    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
