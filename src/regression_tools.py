def hipothesis(theta, features):
	res = 0

	for i, x in enumerate(features):
		res += theta[i] * x

	return res

def derivative_func(data_x, data_y, theta, theta_number):
	summ = 0

	for i, x in enumerate(data_x):
		summ += (hipothesis(theta, x) - data_y[i]) * x[theta_number]
	return (1 / len(data_x)) * summ

def precision_summ(data_x, data_y, theta):
	summ = 0

	for i, x in enumerate(data_x):
		summ += (hipothesis(theta, x) - data_y[i]) ** 2
	return (1 / (2 * len(data_x))) * summ

def run_regression(data, theta):
	validated = parse_array(data, len(theta))
	data_x = validated[0]
	data_y = validated[1]
	precision = precision_summ(data_x, data_y, theta)
	alpha = 0.3
	iterator = 0

	while (condition(theta, precision)):
		theta_copy = theta[:]

		for i, t in enumerate(theta_copy):
			J = derivative_func(data_x, data_y, theta, i)
			theta_copy[i] = theta[i] - alpha * J

		theta = theta_copy[:]
		summNextJ = precision_summ(data_x, data_y, theta)

	return theta

def feature_scaling(data_x, data_y):
	max_array = max(max(data_x))
	max_y = max(data_y)
	max_f = max_y if (max_y > max_array) else max_array

	for i, x_i in enumerate(data_x):
		data_y[i] = data_y[i] / max_f
		for j in range(1, len(x_i)):
			data_x[i][j] = data_x[i][j] / max_f

def condition(theta, precision):
	

def parse_array(data, size):
	data_y = []
	data_x = []

	for j, row in enumerate(data):
		if (len(row) != size):
			print('Warning! Data row -', row, ', size of row is not valid! Deleted from dataset!')
		else:
			for i, elem in enumerate(row):
				if (type(elem) is str):
					row[i] = None

			if (None in row):
				print('Warning! Data row - ', row, ' has non-number values! Deleted from dataset', sep='')
			else:
				data_y.append(row.pop())
				data_x.append([1] + row)

	feature_scaling(data_x, data_y)

	return [data_x, data_y]
