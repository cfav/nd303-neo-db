from enum import Enum
from models import NearEarthObject, OrbitPath
import csv


class OutputFormat(Enum):
    """
    Enum representing supported output formatting options for search results.
    """
    display = 'display'
    csv_file = 'csv_file'

    @staticmethod
    def list():
        """
        :return: list of string representations of OutputFormat enums
        """
        return list(map(lambda output: output.value, OutputFormat))


class NEOWriter(object):
    """
    Python object use to write the results from supported output
    formatting options.
    """

    def __init__(self):
        # TODO: How can we use the OutputFormat in the NEOWriter?
        self.output_format = OutputFormat.list()

    def write(self, format, data, **kwargs):
        """
        Generic write interface that, depending on the OutputFormat selected
        calls the appropriate instance write function

        :param format: str representing the OutputFormat
        :param data: collection of NearEarthObject or OrbitPath results
        :param kwargs: Additional attributes used for formatting output
        e.g. filename

        :return: bool representing if write successful or not
        """
        # TODO: Using the OutputFormat, how can we organize our 'write' logic
        # for output to stdout vs to csvfile
        # TODO: into instance methods for NEOWriter? Write instance methods
        # that write() can call to do the necessary
        # TODO: output format.

        output_choice = self.output_format.index(format)

        if output_choice == 0:
            for row in data:
                print(row)

        elif output_choice == 1:
            with open('results.csv', 'w') as csvfile:
                fieldnames = self.get_fieldnames(data[0])

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

                if type(data[0]) == NearEarthObject:
                    for row in data:
                        writer.writerow({
                            'id': row.id,
                            'neo_reference_id': row.neo_reference_id,
                            'name': row.name,
                            'nasa_jpl_url': row.nasa_jpl_url,
                            'absolute_magnitude_h': row.abs_magnitude_h,
                            'estimated_diameter_min_km': row.diameter_min_km,
                            'estimated_diameter_max_km': row.diameter_max_km,
                            'is_potentially_hazardous': row.is_hazardous,
                            'orbit_dates':
                                NearEarthObject.get_orbit_dates(row.orbits),
                            'miss_distances_km':
                                NearEarthObject.get_miss_distances(row.orbits)
                            })

                else:
                    for row in data:
                        writer.writerow({
                            'id': row.id,
                            'neo_reference_id': row.neo_reference_id,
                            'name': row.name,
                            'km_per_second': row.km_per_second,
                            'km_per_hour': row.km_per_hour,
                            'close_approach_date': row.close_approach_date,
                            'close_approach_date_full':
                                row.close_approach_date_full,
                            'estimated_diameter_min_km': row.diameter_min_km,
                            'estimated_diameter_max_km': row.diameter_max_km,
                            'is_potentially_hazardous': row.is_hazardous,
                            'miss_distance_km': row.miss_distance_km
                            })

        else:
            print("write option not supported")

        return True

    def get_fieldnames(self, obj):
        fieldnames = None

        if type(obj) == NearEarthObject:
            fieldnames = ['id',
                          'neo_reference_id',
                          'name',
                          'nasa_jpl_url',
                          'absolute_magnitude_h',
                          'estimated_diameter_min_km',
                          'estimated_diameter_max_km',
                          'is_potentially_hazardous',
                          'orbit_dates',
                          'miss_distances_km'
                          ]
        else:
            fieldnames = ['id',
                          'neo_reference_id',
                          'name',
                          'km_per_second',
                          'km_per_hour',
                          'close_approach_date',
                          'close_approach_date_full',
                          'estimated_diameter_min_km',
                          'estimated_diameter_max_km',
                          'is_potentially_hazardous',
                          'miss_distance_km'
                          ]

        return fieldnames
