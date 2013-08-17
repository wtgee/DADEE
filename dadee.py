#!/usr/bin/python3

import time
import sys

from observation import Session

class DADEE():
    """Realtime plotting of Arduino light sensor data"""
    def __init__(self):
        self.observation = Session()
