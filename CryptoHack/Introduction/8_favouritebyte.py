#!/usr/bin/env python3

import pwn
import re

secret = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

bytes_secret = bytes.fromhex(secret)

counter = 0 
while True:
	flag = pwn.xor(bytes_secret, counter)
	if re.search("crypto",str(flag)):
		break
	else:
		counter += 1

print(flag)
print(f'The flag was found on loop count: {counter}')