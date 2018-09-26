## Search routines

#### How to use

 
```> python3 main.py -h
usage: main.py [-h] -k KEYWORDS -o {OR,AND} -f FILE

Perform a keyword search query against a file.

optional arguments:
  -h, --help            show this help message and exit
  -k KEYWORDS, --keywords KEYWORDS
                        Space separated keywords to search for
  -o {OR,AND}, --operator {OR,AND}
                        Operator: AND means all keywords have to present, OR
                        means any
  -f FILE, --file FILE  Source file to search against
```

#### Output
```
> python3 main.py -f input -k "Care Quality Commission" -o OR
0,1,2,3,4,5,6

> python3 main.py -f input -k "September 2004" -o OR
9

> python3 main.py -f input -k "general population generally" -o OR
6,8
 
> python3 main.py -f input -k "Care Quality Commission admission" -o AND
1

> python3 main.py -f input -k "general population Alzheimer" -o AND
6
```

#### Testing
```
>  python3 -m unittest 
...usage: python3 -m unittest [-h] -k KEYWORDS -o {OR,AND} -f FILE
python3 -m unittest: error: the following arguments are required: -k/--keywords, -o/--operator, -f/--file
usage: python3 -m unittest [-h] -k KEYWORDS -o {OR,AND} -f FILE
python3 -m unittest: error: the following arguments are required: -k/--keywords, -o/--operator, -f/--file
..
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK

```

The output during the script execution is a valid output when the cli parameters
passed are incorrect. I could have potentially buffer the output but thought it
would reduce the test transparency.