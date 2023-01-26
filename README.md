Pure Python
===========

bash[^1]
----
```bash
python3 test_import.py
# ...
python3 -m module
# ...
```

PERL
----
```perl
# pure_python$ python3
# ...
>>> import module
# ...
>>> module.func_in_module()
# ...
>>> from module import func_in_module
>>> func_in_module()
# ...
>>> import test_import
# ❌ error
# ...
>>> test_import.simple_func()
# ...
>>> import module.__main__
# ❌ error
# [control] + d
```

[^1]: ...pure_python$

