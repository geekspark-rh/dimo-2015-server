from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import sys
import freenect
from itertools import chain
import numpy as np
import time
import array

stop_key = ord('q')
low_m  = 90
high_m = 255
i = 0

def createdepthhandler(server):
    def handledepth(dev, depth, timestamp):
        # global i
        # i += 1
        array1d = depth.flatten()
        # print array1d[0]

        barray = bytearray(array1d)

        server.sendMessage(barray)

    return handledepth
    # for depth.flatten()[0]... converted into a byte array...
    # barray[0] is the least significant byte
    # barray[1] is the most significant byte
    # may need to swap them based on what js typed arrays want

def handlebody(dev, ctx):
    pass
    # global i
    # if i == 1:
        # raise freenect.Kill()

def startloop(server):
    freenect.runloop(depth=createdepthhandler(server))

def main():
    startloop()

if __name__ == '__main__':
    main()
