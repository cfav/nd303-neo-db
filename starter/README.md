# Near Earth Object Database

The Near Earth Object database is a searchable Python 3 command-line interface (CLI) project. This is part of the Udacity Intermediate Python Nanodegree.

# Install

A **Python 3.7** project, no external dependencies are required as all libraries used are a part of the Python standard library.

If you have multiple versions of Python installed on your machine, please be mindful [to set up a virtual environment with Python 3.7](https://docs.python.org/3/library/venv.html).

#### To Setup a Python 3  Virtual  Environment

```python3 -m venv /path/to/new/virtual/environment```

# Usage

To use the project:

1. Clone the project to your local machine
2. Create a virtual environment, named `venv`, with `python3 -m venv venv` in project root
3. Activate the virtual environment with `source venv/bin/activate`
4. Navigate to the `./starter` directory
5. Run `python main.py -h` for an explanation of how to run the project
6. Or try it out yourself!

Example of how to use the interface:

1. Find up to 10 NEOs on Jan 1, 2020 displaying output to terminal

`python main.py display -n 10 --date 2020-01-01`

2. Find up to 10 NEOs from input file 'new_neo_data.csv' between Jan 1, 2020 and Jan 10, 2020 within 5 km from Earth,
exporting to a csv file. Results are written in `results.csv`.

`python main.py csv_file -n 10 -f new_neo_data.csv --start_date 2020-01-01 --end_date 2020-01-10 --filter "distance:>=:5"`

## Requirements

The Near Earth Object Database is a searchable database that, given a csv file of Near Earth Objects data, can perform
data searches. All data results are either displayed to the terminal or output to a csv file.

Some Search Scenarios:

   1.  Find up to some number of unique NEOs on a given date or between start date and end date.
   2.  Find up to some number of unique NEOs on a given date or between start date and end date larger than X kilometers.
   3.  Find up to some number of unique NEOs on a given date or between start date and end date larger than X kilometers
       that were hazardous.
   4.  Find up to some number of unique NEOs on a given date or between start date and end date larger than X kilometers
       that were hazardous and within X kilometers from Earth.

To achieve this functionality the project includes Python objects that represent:
- Near Earth Objects
- Orbit Paths
- A container object for the Near Earth Objects and Orbit Paths
- An object to perform the data search on the container
- An object to write the output format of the search results

## Near Earth Object Data

Each row in the `data/neo_data.csv` represents a single orbit path for a Near Earth Object on a given date.

<details>
 <summary> Each row includes the following attributes: </summary>

```
- id: unique id of the NEO 
- neo_reference_id: NEO reference id 
- name: NEO name 
- nasa_jpl_url: url with NASA info on the NEO 
- absolute_magnitude_h: height of NEO 
- estimated_diameter_min_kilometers: diameter in km min 
- estimated_diameter_max_kilometers: diameter in km max 
- estimated_diameter_min_meters: diameter in m min  
- estimated_diameter_max_meters: diameter in m max  
- estimated_diameter_min_miles: diameter in mi min  
- estimated_diameter_max_miles: diameter in mi max  
- estimated_diameter_min_feet: diameter in ft min  
- estimated_diameter_max_feet: diameter in ft max  
- is_potentially_hazardous_asteroid: true/false if hazaradous  
- kilometers_per_second: km pr s 
- kilometers_per_hour: km per hr 
- miles_per_hour: mi per hr 
- close_approach_date: str of NEO orbit close approach date 
- close_approach_date_full: : str of NEO orbit close approach date 
- miss_distance_astronomical: : how far NEO miss in astronomical units 
- miss_distance_lunar: how far NEO miss in lunar units  
- miss_distance_kilometers: how far NEO miss in km 
- miss_distance_miles: how far NEO miss in mi 
- orbiting_body: body orbiting around 
```

</details>

## Project Organization

The project is broken into the following files:

- `main.py`: Python main script to run the project.
- `database.py`: Python module with database logic (e.g. reading the data, storing the data)
- `exceptions.py`: Python module with any custom exceptions logic
- `models.py` Python module with models -- objects representing `NearEarthObject` and `OrbitPath`
- `search.py`: Python module with search logic (e.g. the different date searchers)
- `writer.py`: Python module with write logic (e.g. write to file, print to terminal)

The project additionally has prewritten tests:

- `tests/test_neo_database.py`: Python unittest module with 8 tests, each requirement has 2 tests.

## Sample Commands

To run your implementation, you can run `main.py` which has been provided to you. Examples of how to run it are below:

```
# For running an example of requirement 1: find a unique number of NEOs on a date that will be displayed to stdout

python main.py display -n 10 --date 2020-01-01

# For running an example of requirement 2: find a unique number of NEOs between dates that are not hazardous. Results will be output to a csv.

python main.py csv_file -n 10 --start_date 2020-01-01 --end_date 2020-01-10 --filter "is_hazardous:=:False"

# For running an example of requirement 3: find a unique number of NEOs between dates that are not hazardous, have a diameter greater than 0.02 units. Results will be output to a csv.

python main.py csv_file -n 10 --start_date 2020-01-01 --end_date 2020-01-10 --filter "is_hazardous:=:False" "diameter:>:0.02"

# For running an example of requirement 4: find a unique number of NEOs between dates that are not hazardous, have a diameter greater than 0.02 units, that were more than 50000 units away. Results will be output to a csv.

python main.py csv_file -n 10 --start_date 2020-01-01 --end_date 2020-01-10 --filter "is_hazardous:=:False" "diameter:>:0.02" "distance:>=:50000"
```


## Bugs

Bugs found in development are documented in `issues.md`. It provides a brief explanation on the problem and the
commit hashes on where it is found and resolved. Looking at the commit history should show which files are modified to resolve the bug. There are no special tools used during debugging. Simple print statements sufficed in tracking what caused the errors.

## Design

#### main.py

This file handles parsing user input to the command line and creating instances to load the database, do search, and write the output. This is largely unchanged from the boilerplate. Just rearranged to be PEP8 compliant. 

#### models.py

This file contains two classes that shows the data model of the objects to be stored in our database. Both classes' `__str__` methods are defined to support printing to stdout.

* **NearEarthObject** - stores NEOs and remembers each of its orbits. This basically maps to the fields given in the csv database noted earlier and are noted in quotes below. All are stored as strings unless otherwise noted. 

```
* id - "id"
* neo_reference_id - "neo_reference_id"
* name - "name"
* nasa_jpl_url - "nasa_jpl_url"
* abs_magnitude_h - "absolute_magnitude_h"
* diameter_min_km - "estimated_diameter_min_kilometers" (stored as float)
* diameter_max_km = "estimated_diameter_max_kilometers" (stored as float)
* is_hazardous = "is_potentially_hazardous_asteroid"
* orbits = list containing OrbitPaths. It is possible that a NEO has orbited the earth several times.
* miss_distances_km = list containing miss distances for each OrbitPath ("miss_distance_kilometers")
```

Helper functions:

```
* update_orbits() - populates the orbits list with OrbitPath objects while loading data
* get_orbit_dates() - converts the OrbitPath objects in the orbits list for readability while printing
* get_miss_distances() - populates the miss_distances_km property for printing
```

&nbsp;

* **OrbitPath** - stores orbits at a given date

```
* id = "id"
* neo_reference_id = "neo_reference_id"
* name = "name"
* km_per_second = "kilometers_per_second"
* km_per_hour = "kilometers_per_hour"
* close_approach_date = "close_approach_date"
* close_approach_date_full = "close_approach_date_full"
* diameter_min_km = "estimated_diameter_min_kilometers" (stored as float)
* diameter_max_km = "estimated_diameter_max_kilometers" (stored as float)
* is_hazardous = "is_potentially_hazardous_asteroid"
* miss_distance_km = "miss_distance_kilometers"
```

#### database.py

This file contains NEODatabase class that is tasked to load objects into a `NEODatabase` object in `database.py`.

The `load_data()` function reads from `data/neo_data.csv` by default. In `main.py`, the file location of "neo_data.csv" is passed directly into your `NEODatabase` object as a String.

It is primarily implemented with two dictionaries:

```
neo_date_db - maps orbit dates to OrbitPath objects passing through that date.
neo_name_db - maps NEO names to NearEarthObject objects.
```

The `csv` module is used to implement the loading. The `csv.DictReader` method is used to load key-value pairs from the data and are passed on to create instances of the models in `models.py`. The `close_approach_date` field is used as key to `neo_date_db` while `name` is used for `neo_name_db`. Since we're keeping track of the names of NEOs that were already loaded, we can track if it orbitted the earth again and we append the associated OrbitPath to the `orbits` list of the NearEarthObject with the same name.


#### search.py

This file contains classes to implement search in our database.

* **DateSearch** - contains an Enum of supported date search types. Our program can handle finding NEOs or orbit paths on a given date or between dates.

* **Query** - class to build query selectors based on parameters given by the user in the command line. This returns a namedtuple that contains:
  * the date search type (between or equals)
  * relevant dates depending on date search type
  * filters (to be used in the Filter class)
  * return object type (NEO or OrbitPath)

* **Filter** - class that implements the filter parameters set by the user. The filters are input by the user in the format `[filter_option:operation:value_of_option]` (e.g. `is_hazardous:=:bool`). The user can submit several filters and the supported options are `is_hazardous`, `diameter`, and `distance`. The task is to parse each of these inputs and convert them to an operation we can apply to our initial results. This is done with several member variables and functions:

```
* Options - dictionary that maps the filter option to the relevant property names of an OrbitPath
* Operators - dictionary that maps the operation input to a comparison function found in the `operator` module (https://docs.python.org/3/library/operator.html#module-operator)
* create_filter_options() - method to parse user input to instantiate a Filter object
* convert_value_type() - converts distance and diameter strings to float to avoid invalid type comparisons
* apply() - compares the value stored in an OrbitPath object to the filter parameters set by the user
```

* **NEOSearcher** - class that implements the search parameters set by the user. This is done with the `get_objects()` method and it follows the following steps:

  1. Collect objects in a given date or between dates. This is done by sorting the dictionary keys of `neo_date_db`. Since the string format uses numbers (e.g. 2020-01-01), we can opt not to convert the data type to something like datetime before sorting. This will have some implications which I will describe later.

  2. Implements filters. This is done by passing the user input to the Filter.create_filter_options() method to construct the operations needed. The objects collected in step 1 are then filtered by passing it to the Filter.apply() function.

  3. Reduce to the number of results set by the user if necessary. The `-n` flag in the user input indicates the number of results to be returned. This is done simply by slicing the list returned in Step 2.

  4. Return results as the return type specified by the user (NEO or Path). This is done by accessing the name property of the OrbitPath results.

  Two helper functions (`get_date_list()` and `get_results()`) are included for readability.

#### writer.py

This file implements a `NEOWriter` class that handles writing the results to stdout or a csv file. It checks which output format is specified by the user. `display` outputs to the console while `csv_file` outputs to a csv file named `results.csv`.  The `csv.DictWriter()` method is used to write results to a csv file named `results.csv`. The fieldnames are obtained by examining the type of the objects in the results.

## Testing
Unit tests are provided in the boilerplate and can be run with `python -m unittest discover`. All tests should pass. This helped in crafting the solution and debugging but there are also several bugs found in this test file itself. These are described in `issues.md`. 

## Development

Basically, the code changes can be chunked into three distinct milestones with regards to the search requirements. The tests are mostly done manually and discrepancies with the test file are fixed towards the end.

  * Search with specified date and number of results.

  	* Commit hash: 3e9160a2dd4a811f81473bd635b2e5be01671656
  	* Design decisions: As mentioned in the boilerplate hints, a dictionary would be a good choice to store our objects. Python dictionaries also have a built-in `get()` method so we don't need to create a separate helper function to extract info from the database. The given search requirements show that the date is needed for each search type so we need a quick way to find the NEOs on that date. We do this by using the `close_approach_date` field in the csv file as keys to create our dictionary (`neo_date_db`). The challenge is linking the NearEarthObject to several orbits and this was done by using the `name` field as keys to another dictionary (`neo_name_db`). This allows us to link several OrbitPath objects to a NearEarthObject. We examine if an incoming OrbitPath object's name is already stored in `neo_name_db` and if so, we append it to the corresponding NearEarthObject's `orbits` list. Shrinking the results to the number of results specified by the user is done easily by just slicing the results list down to the given number.


  * Same as above but with specified start and end dates.

  	* Commit hash: 111c33b046e1c6241ab959afa9a306009ee9dbec
  	* Design decisions: The challenge here is to find the range of dates we can collect NEOs. Upon manual inspection of the input csv, I noticed that the dates are not sorted so these are also unsorted in our dictionary (i.e. Python 3.7 remembers insertion order so no need for an explicit OrderedDict). The problem is solved by sorting the keys of the `neo_date_db` dictionary and storing the results in a list. We find the indices of the start and end dates in this list and we slice it to get the sublist of valid dates to search on. We can now collect our results by iterating through this sublist and getting the objects found during this date.

  * Same as above but with specified filters.

  	* Commit hash: ae72af7b1dd6ac54b003b56d4edace10c4c00bff
  	* Design decisions: My intention was to first solve the `is_hazardous` filter but stumbled upon solving all cases by just solving this one case. As hinted in the boilerplate, the filter options will come in as a list of strings. This means we can also output a list of Filter objects and that means we can solve all cases in one go. The main change I did here is to map the filter_name to the property names in `models.py`. This allows getting the values associated with the object by looking at the filter_name. I also found later on that I need to store the distances and diameters as floats to compare properly and to fit the unittests. Originally, I was storing it as strings and thus, fails some of the cases given.

The rest of the development time is spent mostly on refactoring, documentation and minor bug fixing.

## Unsupported Features

The program has some limitations and an UnsupportedFeature exception is raised when these are encountered:

* Date inputs are not found in the neo_date_db dictionary (e.g. 2000-01-01). Fixing this requires a more complex way of finding the date indices when doing a `between` date search. I don't think this needs to be supported based on the unit test cases provided.
* Return object type specified is neither `NEO` or `Path`.
* Dates are not specified.
* Filter names are neither `is_hazardous`, `distance`, nor `diameter`.
* Output option is neither `display` or `csv_file`.


