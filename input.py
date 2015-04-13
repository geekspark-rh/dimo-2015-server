import sys
import freenect
import time

def createdepthhandler(server):
    def handledepth(dev, depth, timestamp):
        array1d = depth.flatten()
        barray = bytearray(array1d)
        server.sendMessage(barray)

    return handledepth
    # for depth.flatten()[0]... converted into a byte array...
    # barray[0] is the least significant byte
    # barray[1] is the most significant byte
    # may need to swap them based on what js typed arrays want

def startloop(server):
    freenect.runloop(
        depth=createdepthhandler(server)
    )

