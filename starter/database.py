from models import OrbitPath, NearEarthObject
import csv


class NEODatabase(object):
    """
    Object to hold Near Earth Objects and their orbits.

    To support optimized date searching, a dict mapping of all orbit date paths
    to the Near Earth Objects recorded on a given day is maintained.
    Additionally, all unique instances of a Near Earth Object
    are contained in a dict mapping the Near Earth Object name
    to the NearEarthObject instance.
    """

    def __init__(self, filename):
        """
        :param filename: str representing the pathway of the filename
        containing the Near Earth Object data
        """
        self.filename = filename
        self.neo_name_db = {}
        self.neo_date_db = {}

    def load_data(self, filename=None):
        """
        Loads data from a .csv file, instantiating NearEarthObjects
        and their OrbitPaths by:
           - Storing a dict of orbit date to list of NearEarthObject instances
           - Storing a dict of the Near Earth Object name to the single
           instance of NearEarthObject

        :param filename:
        :return:
        """

        if not (filename or self.filename):
            raise Exception('Cannot load data, no filename provided')

        filename = filename or self.filename

        # TODO: Load data from csv file.
        # TODO: Where will the data be stored?
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                neo = NearEarthObject(**row)
                orbit = OrbitPath(**row)
                approach_date = row["close_approach_date"]

                self.neo_name_db.setdefault(neo.name, neo).update_orbits(orbit)
                self.neo_date_db.setdefault(
                    approach_date, []).append(
                    orbit
                    )
