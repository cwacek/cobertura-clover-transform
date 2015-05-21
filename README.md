cobertura-clover-transform
==========================

A tool for transforming Cobertura test coverage XML created by 
[coverage.py](http://nedbatchelder.com/code/coverage/) into Clover-style XML 
which can be displayed by [Atlassian Bamboo](https://www.atlassian.com/software/bamboo).

Install
-------

Running

```sh
python setup.py install
```

will install `cobertura-clover-transform` package and a command-line entry point 
with the same name.

How to run
----------

```sh
cobertura-clover-transform <xml_file>
```

XML transform
-------------

The transform is actually defined using an XSLT, which is stored inside
this repository. Feel free to use it for other purposes.
