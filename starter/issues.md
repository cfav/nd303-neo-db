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