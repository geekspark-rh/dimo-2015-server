import sys
import freenect
import time

def createdepthhandler(server):
    def handledepth(dev, depth, timestamp):
        """Flatten the 2D depth array into a 1D array, convert it into a
        bytearray, and send it to the client."""
        array1d = depth.flatten()
        barray = bytearray(array1d)
        server.sendMessage(barray)

    return handledepth

def startloop(server):
    freenect.runloop(
        depth=createdepthhandler(server)
    )

