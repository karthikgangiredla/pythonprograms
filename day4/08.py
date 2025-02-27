#binary
empty_bytes=bytes()
zero_bytes=bytes(5)
from_string =bytes('Hello',encoding="utf-8")#utf-16,utf-32
b=b'Hello'
type(b)#bytes

from_list = bytes([72, 101, 108, 108, 111])
print(from_list)
l_byte=b'Hello'
l_byte[0]#72

literal_byte = bytearray("Hello", "utf-8")
literal_byte[0] = 71
literal_byte#bytearray(b'Gello')
#memoryview

#view=memoryview(data)
#view[0]=100
