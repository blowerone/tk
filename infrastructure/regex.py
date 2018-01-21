#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

myString = '''
drwxr-xr-x 1 wjk 197121   0  V3.40.20.00B20.BplCpu
drwxr-xr-x 1 wjk 197121   0  V3.40.20.00B20.Ccf0Cpu
drwxr-xr-x 1 wjk 197121   0  V3.40.20.00B20.Cce1Cpu
-rw-r--r-- 1 wjk 197121 373  V3.40.20.00B20.SimoCpu
-rw-r--r-- 1 wjk 197121 431  V3.40.20.00B20.Bpl1Cpu
drwxr-xr-x 1 wjk 197121   0  V3.40.20.00B20.Bp4Cpu
drwxr-xr-x 1 wjk 197121   0  V3.40.20.00B20.B11Cpu
drwxr-xr-x 1 wjk 197121   0  V3.40.20.00B20.B23lCpu
drwxr-xr-x 1 wjk 197121   0  V3.40.20.00B20.Bp78Cpu
'''

# print(myString.split())
# print re.compile(r'Cc\w+Cpu').findall(myString)
print re.compile(r'V.*Cc\w+Cpu').findall(myString)

