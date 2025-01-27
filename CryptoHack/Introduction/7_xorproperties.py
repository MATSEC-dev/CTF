#!/usr/bin/env python3

import pwn

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_KEY1_KEY3_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf" 

KEY1_bytes = bytes.fromhex(KEY1)
KEY2_KEY1_bytes = bytes.fromhex(KEY2_KEY1)
KEY2_KEY3_bytes = bytes.fromhex(KEY2_KEY3)
FLAG_KEY1_KEY3_KEY2_bytes = bytes.fromhex(FLAG_KEY1_KEY3_KEY2)

XOR_KEY2 = pwn.xor(KEY2_KEY1_bytes,KEY1_bytes)
XOR_KEY3 = pwn.xor(KEY2_KEY3_bytes,XOR_KEY2)

# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = bytes
# bytes ^ key2, then prev ^ key3, then prev ^ key1 = flag

XOR_FLAG_KEY2 = pwn.xor(FLAG_KEY1_KEY3_KEY2_bytes,XOR_KEY2)
XOR_FLAG_KEY3 = pwn.xor(XOR_FLAG_KEY2,XOR_KEY3)
XOR_FLAG = pwn.xor(XOR_FLAG_KEY3,KEY1_bytes)

print(XOR_FLAG)
