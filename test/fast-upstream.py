#!/usr/bin/env python
import time
import sys

i = 0
while i < 30000:
    i += 1
    sys.stdout.write('upstream-output: ' + str(i) + '\n')
    sys.stdout.flush()
    if i % 5000 == 0:
        time.sleep(1)

