import freenect
from threading import Thread

last_tilt = 0

class KinectLoop(Thread):

    def __init__(self, server, **kwargs):
        super(KinectLoop, self).__init__(**kwargs)
        self.server = server
        self.killfreenect = False

    def body(self, dev, ctx):
        global last_tilt
        if self.killfreenect:
            raise freenect.Kill("Killing freenect runloop")
        if (self.server.tilt is None or self.server.tilt == last_tilt):
            return
        else:
            freenect.set_tilt_degs(dev, self.server.tilt)
            last_tilt = self.server.tilt

    def kill(self):
        self.killfreenect = True

    def run(self):
        freenect.runloop(body=self.body, depth=createdepthhandler(self.server))


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
