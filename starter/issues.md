## Bug Tracker


**# 1: Output to stdout does not print orbit dates yet.**

* Command to reproduce: `python main.py display -n 10 -d "2020-01-10"`
* Found in commit: 1a40c1208db5761bc9efb11956a96aed2b012ac8
* Resolved in commit: af4a03242ae663291362cf9ca0c44677cef36d35

&nbsp;

**# 2: Looking up orbit paths can be inefficient**

* Details: The previous design of the date database stores NEO objects. That 
requires a list lookup when parsing dates for Orbit Paths and it can introduce
unnecessary complexity.
* Command to reproduce: `python main.py display -n 10 -d "2020-01-10" -r Path`
* Found in commit: 1a2b95a3f4cb9443996b655e4be17f8e8b47efe2
* Resolved in commit: 4a31170db0b2255cc79ce8c0e986a6f1b908342f

&nbsp;

**# 3: NameError when running test file**

* Details: Getting several NameError flags when running test file
* Command to reproduce: `python -m unittest discover`
* Found in commit: b9a510992127db10813c90ca0e64272c016f74aa
* Resolved in commit: 2b6988f710c9d73c860a691e97aefc1d099c6c27

&nbsp;

**# 4: AssertionError in test_find_unique_number_neos_on_date_with_diameter**

* Details: Running command manually works but fails in the unittest
* Command to reproduce: `python -m unittest discover`
* Found in commit: 2b6988f710c9d73c860a691e97aefc1d099c6c27
* Resolved in commit: 4a31170db0b2255cc79ce8c0e986a6f1b908342f

&nbsp;

**# 5: 'NearEarthObject' object has no attribute 'diameter_min_km'**

* Details: test file uses different property names for NearEarthModels and
OrbitPaths.
* Command to reproduce: `python -m unittest discover`
* Found in commit: 2078033a60a442e2ef9e3c0f9bc7693b5a494e0d
* Resolved in commit: 7058bd1251c83fe4926f5410e1e94d5b5d5799dc

&nbsp;

**# 6: TypeError: '>' not supported between instances of 'str' and 'float'**

* Details: invalid comparisons
* Command to reproduce: `python -m unittest discover`
* Found in commit: 7058bd1251c83fe4926f5410e1e94d5b5d5799dc
* Resolved in commit: 3b12a015e458369e8b77df92add460f0fcc6afe2

&nbsp;

**# 7: object has no attribute 'is_potentially_hazardous_asteroid'**

* Details: Tests expect 'is_potentially_hazardous_asteroid' as the property
name.
* Command to reproduce: `python -m unittest discover`
* Found in commit: 3b12a015e458369e8b77df92add460f0fcc6afe2
* Resolved in commit: 05e747f0149e771465fb3ae6f7656c8cc3e5b318

&nbsp;

**# 8: failing tests when there are no matches found**

* Details: Unit tests count the length of the results returned. However, the
current implementation pushes a "NO MATCHES FOUND" string when there are no
matches in the search and that causes a miscount.
* Command to reproduce: `python -m unittest discover`
* Found in commit: 05e747f0149e771465fb3ae6f7656c8cc3e5b318
* Resolved in commit: 05e747f0149e771465fb3ae6f7656c8cc3e5b318


