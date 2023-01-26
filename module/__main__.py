#__main__.py делает директорию модулем для запуска через консоль
#python3 -m console_module

print(f'console_module/__main__.py [__name__ == {__name__}]')
if __name__ == '__main__':
	print('✅ запуск модуля')
else:
	print('❌ запуск модуля: ошибка')

