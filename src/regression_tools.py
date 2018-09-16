def hypothesis(theta, features):
	res = 0

	for i, x in enumerate(features):
		res += theta[i] * x

	return res

def derivative_func(data_x, data_y, theta, theta_number):
	summ = 0

	for i, x in enumerate(data_x):
		summ += (hypothesis(theta, x) - data_y[i]) * x[theta_number]
	return (1 / len(data_x)) * summ

def precision_summ(data_x, data_y, theta):
	summ = 0

	for i, x in enumerate(data_x):
		summ += (hypothesis(theta, x) - data_y[i]) ** 2

	return (1 / (2 * len(data_x))) * summ

def run_regression(data, theta, alpha, J_all, flags):
	validated = parse_array(data, len(theta))
	max_x = get_max(validated[0], validated[1])
	data_x = validated[0]
	data_y = validated[1]
	summPrevJ = 0
	summNextJ = precision_summ(data_x, data_y, theta)
	J_all.append(summNextJ)
	it = 0

	feature_scaling(data_x, data_y)

	while (abs(summPrevJ) >= abs(summNextJ) or summPrevJ == 0):
		summPrevJ = summNextJ
		summNextJ = 0
		theta_copy = theta[:]

		for i, t in enumerate(theta_copy):
			J = derivative_func(data_x, data_y, theta, i)
			theta_copy[i] = theta[i] - alpha * J

		theta = theta_copy[:]
		summNextJ = precision_summ(data_x, data_y, theta)
		J_all.append(summNextJ)
		if (flags[4]):
			print("Precision =", summNextJ)

		it += 1
		if (flags[3] != -1 and it >= flags[3]):
			break

	theta[0] = theta[0] * max_x

	return theta

def feature_scaling(data_x, data_y):
	max_f = get_max(data_x, data_y)

	for i, x_i in enumerate(data_x):
		data_y[i] = data_y[i] / max_f
		if (type(x_i) is list):
			for j in range(1, len(x_i)):
				data_x[i][j] = data_x[i][j] / max_f
		else:
			data_x[i] = data_x[i] / max_f

def get_max(data_x, data_y):
	max_array = max(max(data_x)) if (type(data_x[0]) is list) else max(data_x)
	max_y = max(data_y)
	max_f = max_y if (max_y > max_array) else max_array

	return max_f

def get_min(data_x, data_y):
	min_array = min(min(data_x)) if (type(data_x[0]) is list) else min(data_x)
	min_y = min(data_y)
	min_f = min_y if (min_y < min_array) else min_array

	return min_f

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
				data_y.append(row[-1])
				data_x.append([1] + row[:-1])

	return [data_x, data_y]
