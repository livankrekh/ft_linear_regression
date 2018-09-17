#!./venv/bin/python3

from src.regression_tools import run_regression
from src.tools import *

if __name__ == "__main__":

	try:

		flags = parse_args(sys.argv)
		data = parse_csv(flags[0])
	
	except FileNotFoundError:
		print("\033[1m\033[31mError: file not found!\033[0m")
		exit()
	except OSError as error:
		print("\033[1m\033[31mError: cannot open file ->", error, "\033[0m")
		exit()
	except Exception as error:
		print("\033[1m\033[31mUnknown error:", error, "\033[0m")

	if (type(data[0][0]) is str):
		names = data[:1]
		data = data[1:]

	data_for_viz = data[:]
	J_all = []
	alpha = flags[1]

	try:

		theta = run_regression(data, [0] * len(data[0]), alpha, J_all, flags)
		write_result(theta, len(J_all))

	except KeyboardInterrupt:
		print("\n\033[1mStop training! Exit!\033[0m")
		exit()
	except OSError as err:
		print("\033[1m\033[31mError: cannot create 'model.csv' file!\033[0m")
		exit()
	except Exception as err:
		print("\033[1m\033[31mUnknown error:", err, "\033[0m")
		exit()

	if (flags[2]):
		try:
			vizualize(data_for_viz, theta, J_all, names)
		except UnicodeDecodeError:
			print("\033[1m\033[31mWarning! Catched error from matplotlib (franework bug in MacOS). Please, don't use scroll on graphs\033[0m")
		except KeyboardInterrupt:
			print("\n\033[1mStop vizualize! Exit!\033[0m")
			exit()
