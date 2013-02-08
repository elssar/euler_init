# euler_init

Python script to initalize a file with problem text from a [Project Euler](http://projecteuler.net) problem.

### Usage -

    python euler_init.py problem_number* language file_name
    * required

    In case you don't specify a language, the program will default to Python.
    In case you don't specify a file name, it will be defaulted to the problem number.
    
Requires -

 - [PyYaml](http://pyyaml.org/)
 - [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
 - [Requests](http://docs.python-requests.org/en/latest/)
