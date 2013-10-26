#!/usr/bin/python3

import time
import sys
import ephem

from observation import Session

class DADEE():
    """Realtime plotting of Arduino light sensor data"""
    def __init__(self,location='hilo'):
        self.observation = Session()

        # Add more locations as needed
        self.observer_locations = {
            'hilo': {
                'lon': '-155:05:23:99',
                'lat': '19:42:00:00',
                'elevation': 88 , # meters
                'temp': 23, # celsius
                'pressure': 1010 # This is default but also a guess
             },
            'vis': {
                'lon': '-155:27:52:35', 
                'lat': '19:45:42:96',
                'elevation': 2848.5, # meters
                'temp': 15, # celsius - this is a guess
                'pressure': 700 #this is a guess
            },
        }

        # Building an Observer to watch the moon. Shouldn't need to change anything here. Move along.
        self.observer = ephem.Observer()

        # Get the settings for our location
        location_settings = self.observer_locations[location]
        self.observer.lat = location_settings['lat']
        self.observer.lon = location_settings['lon']
        self.observer.elevation = location_settings['elevation']
        self.observer.temp = location_settings['temp']
        self.observer.pressure = location_settings['pressure']
        self.observer.date = ephem.now()

        # Create our Moon and look at it from our observer location
        self.moon = ephem.Moon(self.observer)


    def get_alt_az(self):
        """ Prints out the current alt/az """

        while True:
            print(self.moon.alt, self.moon.az)
            self.observer.date = ephem.now()
            self.moon.compute(self.observer)
            time.sleep(1)


    def get_good_obs_dates(start_date=ephem.now(),end_date=ephem.Date('2014-01-01')):
        """ 
            Given a start_date and an end_date, loop
            through and find every (night) hour when
            moon is above 20°. Defaults to remainder
            of year.
        """


    def find_nearest_star(obj):
        """
            Finds the star that appears closest to the moon for the observer. The star list
            comes from ephems list of stars of known magnitudes.
        """
        # First calculate the distance for each known star
        for name, star in stars.stars.items():
            star.compute(self.observer)

        # Get the dict of all separations for object
        star_sep = {name:ephem.separation(obj,star) for name,star in stars.stars.items()}
        
        # Get the star with minimum separation
        min_star_name = min(star_sep, key = lambda k: star_sep[k])
        return stars.star(min_star_name)

