import sys
import freenect
import time

def createdepthhandler(server):
    def handledepth(dev, depth, timestamp):
        array1d = depth.flatten()
        barray = bytearray(array1d)
        server.sendMessage(barray)

    return handledepth

def startloop(server):
    freenect.runloop(
        depth=createdepthhandler(server)
    )

