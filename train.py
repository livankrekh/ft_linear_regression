#!./venv/bin/python3

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from src.regression_tools import run_regression, feature_scaling
import numpy as np

import copy
import csv
import sys
import re

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

def vizualize(data, theta, names):
	t = np.arange(0.0, 1.0, 0.001)
	new_data = parse_for_viz(data)

	print(theta)
	plt.plot(t, t * theta[1] + theta[0])
	plt.plot(new_data[0], new_data[1], 'ro')
	plt.grid(True)
	plt.xlabel(names[0])
	plt.ylabel(names[1])
	plt.show()

if __name__ == "__main__":

	if (len(sys.argv) < 2):
		print('Error: no input file!')
		exit()

	data = parse_csv(sys.argv[1])
	theta = [0] * len(data[0])
	names = data[:1][0]
	data = data[1:]
	data_for_viz = data[:]

	theta = run_regression(data, theta)

	print(theta)
	print(theta[1] * data_for_viz[0][0] + theta[0], ". Need - 3650")

	vizualize(data_for_viz, theta, names)
