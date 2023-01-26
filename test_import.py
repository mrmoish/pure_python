# скрипт для теста импорта и прямого запуска

# тест прямого запуска
print(f'test_import.py [__name__ == {__name__}]')
if __name__ == '__main__':
        print('✅ прямой запуск')
else:
        print('❌ прямой запусл: ошибка')

def simple_func():
	print(f"🚀 test_import.py::simple_func()")

simple_func()

# тест импорта
import module
from module import func_in_module

module.func_in_module()
func_in_module()

