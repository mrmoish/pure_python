#__init__.py делает директорию модулем для импорта в другие проекты
#import module
#from module import func_in_module

print(f'module/__init__.py [__name__ == {__name__}]')
if __name__ != '__main__':
	print('✅ импорт')
else:
	print('❌ импорт: ошибка')

def func_in_module():
	print(f'🚀 module/__init__.py::func_in_module()')

