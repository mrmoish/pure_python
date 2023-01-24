# скрипт для теста импорта и прямого запуска

print(f'🚀 test_import.py [__name__ == {__name__}]')
if __name__ == '__main__':
        print('✅✅✅ LAUNCH ✅✅✅')
else:
        print('❌❌❌ error ❌❌❌')


import import_module
from import_module import func_in_module

def simple_func():
	print(f"\t🚀\t test_import.py::simple_func()")

import_module.func_in_module()
func_in_module()
simple_func()

