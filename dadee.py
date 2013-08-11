#!/usr/bin/python3

import time
import sys

import Observation

class DADEE():
    """Realtime plotting of Arduino light sensor data"""
    def __init__(self):
        self.observation = ''
