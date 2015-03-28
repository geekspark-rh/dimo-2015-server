from freenect import sync_get_depth as get_depth, sync_get_video as get_video
from itertools import chain
import numpy as np
import cv
import time
import json


stop_key = ord('q')
low_m  = 90
high_m = 255

class Finder:

    def get_default_tracker(self, h, w):
        return {
            'h'    : h,
            'w'    : w,
            'count': 0,
            'brain': {
                'theta' : 50,
                'alpha' : 25
            },
            'red'  : {'x': 0, 'y': 0},
            'green': {'x': 0, 'y': 0},
            'blue' : {'x': 0, 'y': 100}
        }

    def init(self, server, opts):
        print("inside init")
        fps = 30 # frames per second
        duration = 1000.0 / fps # duration of each frame in ms

        while(True):

            # Get a fresh frame
            (depth,_) = get_depth()

            start = time.time()

            # loop over each color
            flatlist = list(chain.from_iterable(depth.tolist()))
            server.sendMessage(json.dumps(flatlist))

            time.sleep(1) # seconds

            end = time.time()

