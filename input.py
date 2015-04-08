from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import freenect
from itertools import chain
import numpy as np
import time
import array

stop_key = ord('q')
low_m  = 90
high_m = 255

def handledepth(dev, depth, timestamp):
    server.sendMessage(depth)

def startloop():
    freenect.runloop(depth=handledepth)

def main():
    startloop()

if __name__ == '__main__':
    main()
