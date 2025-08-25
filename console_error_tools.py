def finish(catagory, *message, hint=''):
	print('\033[96m*', '~' * 64, '*\033[0m')
	print('\033[1m\033[92m' + catagory + '\033[0m: \033[92m' + ' '.join(message) + '\033[0m')
	if hint: print('-->', hint, '<--')
	print('\033[96m*', '~' * 64, '*\033[0m')
	exit(0)

def warning(catagory, *message, hint=''):
	print('\033[93m*', '~' * 64, '*\033[0m')
	print('\033[1m\033[95m' + catagory + '\033[0m: \033[95m' + ' '.join(message) + '\033[0m')
	if hint: print('-->', hint, '<--')
	print('\033[93m*', '~' * 64, '*\033[0m')

def fumble(catagory, *message, hint=''):
	print('\033[93m*', '~' * 64, '*\033[0m')
	print('\033[1m\033[91m' + catagory + '\033[0m: \033[91m' + ' '.join(message) + '\033[0m')
	if hint: print('-->', hint, '<--')
	print('\033[93m*', '~' * 64, '*\033[0m')

def error(catagory, *message, hint=''):
	print('\033[95m*', '~' * 64, '*\033[0m')
	print('\033[1m\033[91m' + catagory + '\033[0m: \033[91m' + ' '.join(message) + '\033[0m')
	if hint: print('-->', hint, '<--')
	print('\033[95m*', '~' * 64, '*\033[0m')
	exit(1)
