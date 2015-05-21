cobertura-clover-transform
==========================

Tools for transforming Cobertura test coverage XML into Clover-style XML

As it turns out, the coverage created by [coverage.py](http://nedbatchelder.com/code/coverage/)
outputs in Cobertura.

[Bamboo](https://www.atlassian.com/software/bamboo) has built in
support for displaying Clover test coverage output.

This tool can be used to convert Coverage.py output to a format
Bamboo can display.

To run
------

Easy peasy::

    python -m cobertura_clover_transform.converter <xml_file>

The XML
-------

The transform is actually defined using an XSLT, which is inside
this repository. Feel free to use it for other purposes.
