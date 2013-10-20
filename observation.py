#!/usr/bin/python3

import ephem

class Session():
    """Details about a particular observation session night"""
    def __init__(self):
        # initialize the iteration counter
        self.date = ephem.now()

if __name__=='__main__':
    print("Nothing to see. Run the dadee.py file")
