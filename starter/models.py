class NearEarthObject(object):
    """
    Object containing data describing a Near Earth Object and it's orbits.

    # TODO: You may be adding instance methods to NearEarthObject to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given Near Earth Object, only a subset of attributes used
        """
        # TODO: What instance variables will be useful for storing on the Near Earth Object?
        self.id = kwargs["id"]
        self.neo_reference_id = kwargs["neo_reference_id"]
        self.name = kwargs["name"]
        self.nasa_jpl_url = kwargs["name"]
        self.absolute_magnitude_h = kwargs["absolute_magnitude_h"]
        self.estimated_diameter_min_kilometers = kwargs["estimated_diameter_min_kilometers"]
        self.estimated_diameter_max_kilometers = kwargs["estimated_diameter_max_kilometers"]
        self.is_potentially_hazardous_asteroid = kwargs["is_potentially_hazardous_asteroid"]
        self.close_approach_date_full = kwargs["close_approach_date_full"]
        self.orbits = []

    def __str__(self):
        neo_contents =  f'id = {self.id}\n' + \
                        f'name = {self.name}\n' + \
                        f'orbit dates = {self.get_orbit_dates()}\n'
        return neo_contents


    def update_orbits(self, orbit):
        """
        Adds an orbit path information to a Near Earth Object list of orbits

        :param orbit: OrbitPath
        :return: None
        """

        # TODO: How do we connect orbits back to the Near Earth Object?
        self.orbits.append(orbit)

    def get_orbit_dates(self):
        """
        Extracts the dates from the NEO instance

        :return: list of dates
        """
        orbit_dates = []

        for orbit in self.orbits:
            orbit_dates.append(orbit.close_approach_date_full)

        return orbit_dates



class OrbitPath(object):
    """
    Object containing data describing a Near Earth Object orbit.

    # TODO: You may be adding instance methods to OrbitPath to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given orbit, only a subset of attributes used
        """
        # TODO: What instance variables will be useful for storing on the Near Earth Object?
        self.id = kwargs["id"]
        self.neo_reference_id = kwargs["neo_reference_id"]
        self.name = kwargs["name"]
        self.kilometers_per_second = kwargs["kilometers_per_second"]
        self.kilometers_per_hour = kwargs["kilometers_per_hour"]
        self.close_approach_date = kwargs["close_approach_date"]
        self.close_approach_date_full = kwargs["close_approach_date_full"]
        self.miss_distance_astronomical = kwargs["miss_distance_astronomical"]
        self.miss_distance_lunar = kwargs["miss_distance_lunar"]
        self.miss_distance_kilometers = kwargs["miss_distance_kilometers"]
        self.miss_distance_miles = kwargs["miss_distance_miles"]
