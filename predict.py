#!/usr/local/bin/python3

import sys
import csv

if __name__ == "__main__":
	model = []
	args = []
	res = 0

	if (len(sys.argv) < 2):
		print("\033[1m\033[31mError: no enter args!\033[0m")

	try:
		with open('./model/model.csv') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				for theta in row:
					model.append(float(theta))
	except OSError:
		print('\033[1m\033[31mError: can\'t open model file (model/model.csv)\033[0m')
	except (ValueError, IndexError):
		print('\033[1m\033[31mError: not valid model file (model/model.csv)\033[0m')
	except Exception as err:
		print('\033[1m\033[31mUnknown error:', err, '\033[0m')

	args = sys.argv
	args[0] = 1

	if (len(args) < len(model)):
		print("\033[1mWarning! Not enough arguments, ignored! By default other args = 0\033[0m")
		args += [0] * (len(model) - len(args))

	try:
		for i, theta in enumerate(model):
			res += theta * float(args[i])
	except ValueError:
		print('\033[1m\033[31mError: arguments can be only number!\033[0m')

	print("\033[1m\033[32mResult =", res, "\033[0m")
