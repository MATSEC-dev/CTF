#!/usr/bin/env python3

import pwn

encrypted_flag = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'

bytes_flag = bytes.fromhex(encrypted_flag)

sample_flag = 'crypto{'

xored_sample_flag = pwn.xor(bytes_flag, sample_flag)

print(xored_sample_flag)
# Outputed data: b'myXORke+y_Q\x0bHOMe$~seG8bGURN\x04DFWg)a|\x1dTM!an\x7f'

key = 'myXORkey'
xored_sample_flag = pwn.xor(bytes_flag, key)
print(xored_sample_flag)