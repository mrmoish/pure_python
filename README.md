README
======

bash[1^]
----
```console
$ python3 test_import.py[1^]
# ...
```

PERL[1^]
----
```console
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


[^1]: pwd = .../pure_python

