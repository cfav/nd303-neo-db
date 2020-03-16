from operator import eq, gt, lt, le, ge
from datetime import datetime as dt

from collections import namedtuple
from enum import Enum

from exceptions import UnsupportedFeature
from models import NearEarthObject, OrbitPath


class DateSearch(Enum):
    """
    Enum representing supported date search on Near Earth Objects.
    """
    between = 'between'
    equals = 'equals'

    @staticmethod
    def list():
        """
        :return: list of string representations of DateSearchType enums
        """
        return list(map(lambda output: output.value, DateSearch))


class Query(object):
    """
    Object representing the desired search query operation to build.
    The Query uses the Selectors to structure the query information into
    a format the NEOSearcher can use for date search.
    """

    Selectors = namedtuple(
        'Selectors',
        ['date_search', 'number', 'filters', 'return_object']
        )
    DateSearch = namedtuple(
        'DateSearch',
        ['type', 'values']
        )
    ReturnObjects = {'NEO': NearEarthObject, 'Path': OrbitPath}

    def __init__(self, **kwargs):
        """
        :param kwargs: dict of search query parameters to determine
        which SearchOperation query to use
        """
        self.date = kwargs.get("date", None)
        self.start_date = kwargs.get("start_date", None)
        self.end_date = kwargs.get("end_date", None)
        self.number = kwargs.get("number", 0)
        self.filters = kwargs.get("filter", None)
        self.return_object = kwargs.get("return_object", "NEO")
        self.date_search = {}

    def build_query(self):
        """
        Transforms the provided query options, set upon initialization,
        into a set of Selectors that the NEOSearcher
        can use to perform the appropriate search functionality

        :return: QueryBuild.Selectors namedtuple that translates
        the dict of query options into a SearchOperation
        """
        if self.return_object not in self.ReturnObjects:
            raise UnsupportedFeature

        if self.date:
            self.date_search["type"] = DateSearch.equals.value
            self.date_search["date"] = self.date

        elif self.start_date and self.end_date:
            self.date_search = {
                "type": DateSearch.between.value,
                "start_date": self.start_date,
                "end_date": self.end_date
                }
            self.date_search["filter"] = self.filters

        else:
            raise UnsupportedFeature

        query = self.Selectors(
            self.date_search,
            self.number,
            self.filters,
            self.return_object
            )

        return query


class Filter(object):
    """
    Object representing optional filter options to be used in the date search
    for Near Earth Objects. Each filter is one of Filter.Operators provided
    with a field to filter on a value.
    """

    # TODO: Create a dict of filter name to the NearEarthObject or OrbitPath
    Options = {
        "is_hazardous": "is_hazardous",
        "diameter": "est_dia_min_km",
        "distance": "miss_distance_km"
    }

    # TODO: Create a dict of operator symbol to an Operators method,
    # see README Task 3 for hint
    Operators = {
        "=": eq,
        "<": lt,
        ">": gt,
        ">=": ge,
        "<=": le
    }

    def __init__(self, field, object, operation, value):
        """
        :param field:  str representing field to filter on
        :param object:  object to filter on
        :param operation: str representing filter operation to perform
        :param value: str representing value to filter for
        """
        self.field = field
        self.object = object
        self.operation = operation
        self.value = value

    @staticmethod
    def create_filter_options(filter_options):
        """
        Class function that transforms filter options raw input into filters

        :param input: list in format:
        ["filter_option:operation:value_of_option", ...]

        :return: defaultdict with key of NearEarthObject
        or OrbitPath and value of empty list or list of Filters
        """

        # TODO: return a defaultdict of filters with key of NearEarthObject
        # or OrbitPath and value of empty list or list of Filters

        filters = {}

        for filter_option in filter_options:
            params = filter_option.split(":")
            filter_name = params[0]
            operator = params[1]
            value = params[2]

            if filter_name in Filter.Options:

                filters[Filter.Options[filter_name]] = [Filter(filter_name, None, Filter.Operators[operator], value)]

            else:
                raise UnsupportedFeature

        return filters

    def apply(self, results):
        """
        Function that applies the filter operation onto a set of results

        :param results: List of Near Earth Object results
        :return: filtered list of Near Earth Object results
        """
        # TODO: Takes a list of NearEarthObjects
        # and applies the value of its filter operation to the results
        filtered_results = []

        for result in results:
            self.object = result
            if self.operation(getattr(self.object, Filter.Options[self.field]), self.value):
                filtered_results.append(result)

        return filtered_results


class NEOSearcher(object):
    """
    Object with date search functionality on Near Earth Objects
    exposed by a generic search interface get_objects, which, based on
    the query specifications, determines how to perform the search.
    """

    def __init__(self, db):
        """
        :param db: NEODatabase holding the NearEarthObject instances
        and their OrbitPath instances
        """
        self.db = db
        # TODO: What kind of an instance variable can we use to connect
        # DateSearch to how we do search?
        self.date_search_type = DateSearch.list()

    def get_objects(self, query):
        """
        Generic search interface that, depending on the details
        in the QueryBuilder (query) calls the appropriate instance search
        function, then applys any filters, with distance as the last filter.

        Once any filters provided are applied, return the number of requested
        objects in the query.return_object
        specified.

        :param query: Query.Selectors object with query information
        :return: Dataset of NearEarthObjects or OrbitalPaths
        """
        # TODO: This is a generic method that will need to understand,
        # using DateSearch, how to implement search
        # TODO: Write instance methods that get_objects can use to implement
        # the two types of DateSearch your project
        # TODO: needs to support that then your filters can be applied to.
        # Remember to return the number specified in
        # TODO: the Query.Selectors as well as in the return_type
        # from Query.Selectors

        results = []

        query_date_search_type = query.date_search.get("type", "")
        query_start_date = query.date_search.get("start_date", None)
        query_end_date = query.date_search.get("end_date", None)
        query_date = query.date_search.get("date", None)
        query_db = self.db.neo_date_db

        query_type_index = self.date_search_type.index(query_date_search_type)

        if query_type_index == 0:

            if ((query_start_date in query_db) and
               (query_end_date in query_db)):

                date_list = get_date_list(query_db, start_date, end_date)
                results = get_results(query_db, date_list)
                
            else:
                raise UnsupportedFeature

        elif query_type_index == 1:
            results = query_db.get(query_date)

        if query.filters:
            filters = Filter.create_filter_options(query.filters)

            for key, filter in filters.items():
                results = filter[0].apply(results)

        results = results[:query.number]

        if query.return_object == 'NEO':
            results = list(map(lambda
                              orbit: self.db.neo_name_db[orbit.name],
                              results))
        return results

    @staticmethod
    def get_date_list(db, start_date, end_date):
        """
        Helper function to get a range of dates in the database.

        :param db: NEODatabase object that uses date strings as keys
        :param start_date: str representing start date
        :param end_date: str representing end date
        :return: list of date strings
        """
        date_list = sorted(db)
        start_index = date_list.index(start_date)
        end_index = date_list.index(end_date)
        date_list = date_list[start_index:end_index+1]
        return date_list

    @staticmethod
    def get_results(db, date_list):
        """
        Helper function to get a list of OrbitPaths found on given dates

        :param db: NEODatabase object that uses date strings as keys
        :param date_list: list of date strings
        :return: list of OrbitPaths
        """
        results = []

        for date in date_list:
            orbits = query_db[date]
            for orbit in orbits:
                results.append(orbit)

        return results
