README
======
> pwd = .../pure_python

bash
----
```
$ python3 test_import.py
```

PERL
____
```
$ python3
# ...
>>> import import_module
# ...
>>> import_module.func_in_module()
# ...
>>> from import_module import func_in_module
>>> func_in_module()
# ...
>>> import test_import
# ❌❌❌ error ❌❌❌
# ...
>>> test_import.simple_func()
# ...
# [control] + d
```
