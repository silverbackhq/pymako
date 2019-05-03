PyMako
======

A Consul Client for Python.

[![Build Status](https://travis-ci.org/Clivern/PyMako.svg?branch=master)](https://travis-ci.org/Clivern/PyMako)
[![PyPI version](https://badge.fury.io/py/pymako.svg)](https://badge.fury.io/py/pymako)

Installation
------------
To install PyMako run this command:
```
$ pip3 install pymako
```

Usage
-----
After installing the library, Read the following usage criteria:

```python
from pymako import KV
from pymako import Status


# KV Store Module
kv = KV("http://127.0.0.1:8500")
kv.get("key")
kv.update("key", "value")
kv.delete("key")

# Status Module
status = Status("http://127.0.0.1:8500")
status.leader()
status.peers()
```

Misc
====

Changelog
---------

Version 0.0.1:
```
Initial Release.
```

Acknowledgements
----------------

© 2019, Clivern. Released under [MIT License](https://opensource.org/licenses/mit-license.php).

**PyMako** is authored and maintained by [@clivern](http://github.com/clivern).
