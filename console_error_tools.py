TEXT_RED = '\033[91m'
TEXT_YELLOW = '\033[93m'
TEXT_PINK = '\033[95m'
TEXT_CYAN = '\033[96m'
TEXT_GREEN = '\033[92m'

FORMAT_BOLD = '\033[1m'
FORMAT_END = '\033[0m'

def finish(catagory: str, *message: str, hint: str = ''):
	'''Shows a final message and exits the program'''
	print(TEXT_CYAN + '*', '~' * 64, '*' + FORMAT_END)
	print(FORMAT_BOLD + TEXT_GREEN + catagory + FORMAT_END + ': ' + TEXT_GREEN + ' '.join(message) + FORMAT_END)
	if hint: print('-->', hint, '<--')
	print(TEXT_CYAN + '*', '~' * 64, '*' + FORMAT_END)
	exit(0)

def note(catagory: str, *message: str, hint: str = ''):
	'''Shows a general message'''
	print(TEXT_CYAN + '*', '~' * 64, '*' + FORMAT_END)
	print(FORMAT_BOLD + TEXT_PINK + catagory + FORMAT_END + ': ' + TEXT_PINK + ' '.join(message) + FORMAT_END)
	if hint: print('-->', hint, '<--')
	print(TEXT_CYAN + '*', '~' * 64, '*' + FORMAT_END)

def warning(catagory: str, *message: str, hint: str = ''):
	'''Shows a warning message'''
	print(TEXT_YELLOW + '*', '~' * 64, '*' + FORMAT_END)
	print(FORMAT_BOLD + TEXT_PINK + catagory + FORMAT_END + ': ' + TEXT_PINK + ' '.join(message) + FORMAT_END)
	if hint: print('-->', hint, '<--')
	print(TEXT_YELLOW + '*', '~' * 64, '*' + FORMAT_END)

def fumble(catagory: str, *message: str, hint: str = ''):
	'''Shows a error message without exiting the program'''
	print(TEXT_YELLOW + '*', '~' * 64, '*' + FORMAT_END)
	print(FORMAT_BOLD + TEXT_RED + catagory + FORMAT_END + ': ' + TEXT_RED + ' '.join(message) + FORMAT_END)
	if hint: print('-->', hint, '<--')
	print(TEXT_YELLOW + '*', '~' * 64, '*' + FORMAT_END)

def error(catagory: str, *message: str, hint: str = ''):
	'''Shows a error message and exits the program'''
	print(TEXT_PINK + '*', '~' * 64, '*' + FORMAT_END)
	print(FORMAT_BOLD + TEXT_RED + catagory + FORMAT_END + ': ' + TEXT_RED + ' '.join(message) + FORMAT_END)
	if hint: print('-->', hint, '<--')
	print(TEXT_PINK + '*', '~' * 64, '*' + FORMAT_END)
	exit(1)
