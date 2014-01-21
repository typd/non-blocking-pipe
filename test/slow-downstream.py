#!/usr/bin/env python
import sys
import time

i = 0
for line in sys.stdin:
    sys.stdout.write('downstream-got: ' + line)
    sys.stdout.flush()
    i += 1
    if i % 2500 == 0:
        time.sleep(1)

