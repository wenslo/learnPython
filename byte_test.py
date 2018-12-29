import base64
import struct

n = 10240099
b1 = (n & 0xff000000) >> 24
print(b1)
# print((n & 0xff0000))
b2 = (n & 0xff0000) >> 16
print(b2)
b3 = (n & 0xff00) >> 8
print(b3)
b4 = n & 0xff
print(b4)
bs = bytes([b1, b2, b3, b4])
print(bs)
# 11111111000000000000000000000000
# 111111110000000000000000
# 100111000100000001100011
# 100111000000000000000000
# pack的第一个参数是处理指令，'>I'的意思是：
#
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
v1 = struct.pack('>I', 10240099)
print(v1)
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
v2 = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(v2)

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
v3 = struct.unpack('<ccIIIIIIHH', s)

# print(v3)

bmp_data = base64.b64decode(
    'Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')


def bmp_info(data):
    data = data[:30]
    v4 = struct.unpack('<ccIIIIIIHH', data)
    print(v4)
    if v4[0] == b'B' and v4[1] == b'M':
        print('This file is bmp')
        print(v4)
        return {
            'width': v4[6],
            'height': v4[7],
            'color': v4[9]
        }
    else:
        raise ValueError("file is not bpm")


# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')
