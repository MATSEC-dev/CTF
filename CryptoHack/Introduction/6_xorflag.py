#!/usr/bin/env python3


label_string = 'label'
number_integer = 13 

string_to_integer = []
for i in label_string:
    string_to_integer.append(ord(i))

xored_values = []
for i in string_to_integer:
    xored_values.append(number_integer ^ i)

xored_to_string = []
for i in xored_values:
    xored_to_string.append(chr(i))
print(''.join(xored_to_string))
