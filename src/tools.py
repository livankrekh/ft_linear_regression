import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

from src.regression_tools import feature_scaling, get_max, get_min

import decimal
import csv
import sys
import re
import os

def parse_args(args):
	res = ["", 0.1, False, -1, False]

	for arg in args:
		if (arg.find("--alpha=") != -1):
			arg = arg.replace("--alpha=", '')
			try:
				res[1] = abs(float(arg))
			except ValueError:
				print("\033[1mWarning! Alpha is not defined as number! By default alpha = 0.1\033[0m")
		elif (arg.find('--iter=') != -1):
			arg = arg.replace("--iter=", '')
			try:
				res[3] = int(float(arg))
			except ValueError:
				print("\033[1mWarning! Iter is not defined as number!\033[0m")
		elif (arg == '-v'):
			res[2] = True
		elif (arg == '-p'):
			res[4] = True
		else:
			if (res[0] == ""):
				res[0] = arg

	return res


def parse_csv(file_name):
	regex = re.compile('\-?\d+\.?\d*')

	results = []
	with open(sys.argv[1]) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			new_row = []
			for elem in row:
				if (regex.match(elem)):
					new_row.append(float(elem))
				else:
					new_row.append(elem)
			results.append(new_row)
	return results

def parse_for_viz(data):
	data_x = []
	data_y = []

	for elem in data:
		if (type(elem[-1]) is not str):
			data_y.append(elem.pop())
			data_x.append(elem.pop())

	return [data_x, data_y]

def floatToStr(n):
	ctx = decimal.Context()
	ctx.prec = 20

	d1 = ctx.create_decimal(repr(n))
	return format(d1, 'f')

def vizualize(data, theta, J_all, names):
	new_data = parse_for_viz(data)
	t = np.arange(get_min(new_data[0], new_data[1]), get_max(new_data[0], new_data[1]))
	x = np.arange(0, len(J_all))
	figure = plt.figure()
	grid = gridspec.GridSpec(ncols=2, nrows=2)
	first = figure.add_subplot(grid[0, 0:])
	second = figure.add_subplot(grid[1, 0:])

	first.plot(t, t * theta[1] + theta[0])
	first.plot(new_data[0], new_data[1], 'ro')
	first.grid(True)
	first.set_title("Model view")

	second.plot(x, J_all, 'ro')
	second.grid(True)
	second.set_title("Cost function iteration")

	figure.tight_layout()
	plt.show()

def write_result(theta, J_size):
	print("\033[1m\033[32mModel trained in", J_size, "cycles!")

	os.makedirs(os.path.dirname("./model/model.csv"), exist_ok=True)
	with open('./model/model.csv', 'w') as csvfile:
		for i, t in enumerate(theta):
			csvfile.write(floatToStr(t) + (',' if (i < len(theta) - 1) else ''))
			print(floatToStr(t) + (" * X" + str(i) if (i != 0) else '') + (' + ' if (i < len(theta) - 1) else ''), end='')

	print('\033[0m\n', end='')
