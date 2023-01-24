#__init__.py делает директорию модулем для импорта в другие проекты
#import import_module
#from import_module import

print(f'🚀 import_module/__init__.py [__name__ == {__name__}]')
if __name__ != '__main__':
	print('✅✅✅ IMPORT ✅✅✅')
else:
	print('❌❌❌ error ❌❌❌')

def func_in_module():
	print(f'\t🚀\t import_module/__init__.py::func_in_module()')

