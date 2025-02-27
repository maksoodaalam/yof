def is_number(arg):
	try:
		float(arg)
		return True
	except:
		return False


def is_positive(arg):
	try:
		if isinstance(arg, (float, int)):
			if arg > 0 or arg == 0:
				return True
			else:
				return False
		else:
			return False
	except:
		return False


def is_integer(value):
	if not (value == int(value)):
		return False
	else:
		return True

