#!/usr/local/bin/python3

from src.regression_tools import run_regression

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

if __name__ == "__main__":

	if (len(sys.argv) < 2):
		print('Error: no input file!')
		exit()

	data = parse_csv(sys.argv[1])
	theta = [0] * len(data[0])
	names = data[:1]
	data = data[1:]
	data_for_viz = data[:]

	theta = run_regression(data, theta)

	print(theta)
	print(theta[0] + theta[1] * data_for_viz[0][0], ". Need - 3650")
