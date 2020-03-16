class NearEarthObject(object):
    """
    Object containing data describing a Near Earth Object and it's orbits.

    # TODO: You may be adding instance methods to NearEarthObject
    to help you implement search and output data.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given Near Earth Object,
        only a subset of attributes used
        """
        self.id = kwargs["id"]
        self.neo_reference_id = kwargs["neo_reference_id"]
        self.name = kwargs["name"]
        self.nasa_jpl_url = kwargs["nasa_jpl_url"]
        self.abs_magnitude_h = kwargs["absolute_magnitude_h"]
        self.est_dia_min_km = kwargs["estimated_diameter_min_kilometers"]
        self.est_dia_max_km = kwargs["estimated_diameter_max_kilometers"]
        self.is_hazardous = kwargs["is_potentially_hazardous_asteroid"]
        self.orbits = []
        self.miss_distances_km = []

    def __str__(self):
        neo_contents = f'id = {self.id}\n' + \
                       f'name = {self.name}\n' + \
                       f'absolute magnitude(h) = {self.abs_magnitude_h}\n' + \
                       f'est. diameter min(km) = {self.est_dia_min_km}\n' +\
                       f'est. diameter max(km) = {self.est_dia_max_km}\n' +\
                       f'is hazardous = {self.is_hazardous}\n' +\
                       f'orbit dates = {self.get_orbit_dates(self.orbits)}\n' +\
                       f'miss distances(km) = {self.get_miss_distances(self.orbits)}\n'
        return neo_contents

    def update_orbits(self, orbit):
        """
        Adds an orbit path information to a Near Earth Object list of orbits

        :param orbit: OrbitPath
        :return: None
        """
        # TODO: How do we connect orbits back to the Near Earth Object?
        self.orbits.append(orbit)

    @staticmethod
    def get_orbit_dates(orbits):
        """
        Extracts the dates from the NEO instance

        :return: list of dates
        """
        orbit_dates = []

        for orbit in orbits:
            orbit_dates.append(orbit.close_approach_date_full)

        return orbit_dates

    @staticmethod
    def get_miss_distances(orbits):
        """
        Extracts the dates from the NEO instance

        :return: list of dates
        """
        miss_distances = []

        for orbit in orbits:
            miss_distances.append(orbit.miss_distance_km)

        return miss_distances


class OrbitPath(object):
    """
    Object containing data describing a Near Earth Object orbit.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs:    dict of attributes about a given orbit,
        only a subset of attributes used
        """
        self.id = kwargs["id"]
        self.neo_reference_id = kwargs["neo_reference_id"]
        self.name = kwargs["name"]
        self.km_per_second = kwargs["kilometers_per_second"]
        self.km_per_hour = kwargs["kilometers_per_hour"]
        self.close_approach_date = kwargs["close_approach_date"]
        self.close_approach_date_full = kwargs["close_approach_date_full"]
        self.est_dia_min_km = kwargs["estimated_diameter_min_kilometers"]
        self.est_dia_max_km = kwargs["estimated_diameter_max_kilometers"]
        self.is_hazardous = kwargs["is_potentially_hazardous_asteroid"]
        self.miss_distance_km = kwargs["miss_distance_kilometers"]

    def __str__(self):
        orbit_contents = f'name = {self.name}\n' + \
                         f'miss distance(km) = {self.miss_distance_km}\n' + \
                         f'km per hour = {self.km_per_hour}\n' + \
                         f'est. diameter min(km) = {self.est_dia_min_km}\n' +\
                         f'est. diameter max(km) = {self.est_dia_max_km}\n' +\
                         f'is hazardous = {self.is_hazardous}\n' +\
                         f'orbit date = {self.close_approach_date_full}\n'
        return orbit_contents
