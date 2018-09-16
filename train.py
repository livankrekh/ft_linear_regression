#!./venv/bin/python3

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from src.regression_tools import run_regression, feature_scaling
import numpy as np

import copy
import csv
import sys
import re

def parse_args(args):
	res = ["", 0.1, False]

	for arg in args:
		if (arg.find("--alpha=") != -1):
			arg = arg.replace("--alpha=", '')
			try:
				res[1] = abs(float(arg))
			except ValueError:
				print("\033[1mWarning! Alpha is not defined as number! By default alpha = 0.1\033[0m")
		elif (arg == '-v'):
			res[2] = True
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

	feature_scaling(data_x, data_y)

	return [data_x, data_y]

def vizualize(data, theta, J_all, names):
	t = np.arange(0.0, 1.0, 0.001)
	new_data = parse_for_viz(data)
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


if __name__ == "__main__":

	flags = parse_args(sys.argv)

	data = parse_csv(flags[0])
	names = data[:1]
	data = data[1:]
	data_for_viz = data[:]
	J_all = []
	alpha = flags[1]

	theta = run_regression(data, [0] * len(data[0]), alpha, J_all)

	
	print("\033[1m\033[32mModel trained in", len(J_all), "cycles!\033[0m")

	if (flags[2]):
		vizualize(data_for_viz, theta, J_all, names)
