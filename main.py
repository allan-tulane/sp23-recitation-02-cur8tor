"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	if n == 1:
	 return a * 1 - n
	else:
	 return a * simple_work_calc((n // b), a, b) + n

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 311
	assert simple_work_calc(30, 4, 2) == 1162

	# 3 added tests
	assert simple_work_calc(40, 2, 2) == 224
	assert simple_work_calc(50, 3, 2) == 1124
	assert simple_work_calc(60, 4, 2) == 4708

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n == 1:
	 return a * 1 - f(n)
	else:
	 return a * work_calc((n // b), a, b, f) + f(n)

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	if n == 1:
	 return a * 1 - f(n)
	else:
	 return work_calc((n // b), a, b, f) // a + f(n)

def test_work():
	""" done. """
	assert work_calc(10, 2, 2,lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 529
	assert work_calc(30, 3, 2, lambda n: n) == 381

	# 3 added work tests
	assert work_calc(40, 2, 2,lambda n: 1) == 63
	assert work_calc(50, 1, 2, lambda n: n*n) == 3314
	assert work_calc(60, 3, 2, lambda n: n) == 1203

def compare_work(work_fn1, work_fn2, input_sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in input_sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions that can be passed to compare_work

	# create work_fn1
	# create work_fn2
	# create work_fn3
	work_fn1 = lambda n: work_calc(n, 3, 2, lambda n: 1)
	work_fn2 = lambda n: work_calc(n, 3, 2, lambda n: n)
	work_fn3 = lambda n: work_calc(n, 3, 2, lambda n: n*n)

	# print compare work test 1
	print("compare fn1 with fn2")
	res = compare_work(work_fn1, work_fn2)
	print_results(res)

	# print compare work test 2
	print("compare fn1 with fn3")
	res = compare_work(work_fn1, work_fn3)
	print_results(res)

	# print compare work test 3
	print("compare fn3 with fn2")
	res = compare_work(work_fn3, work_fn2)
	print_results(res)

def print_results_span(results):
	print(tabulate.tabulate(results,
							headers=['1', '2', '4', '8', '16'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_span():
	# TODO
	n_list = list()
	for n in [10, 20, 50, 100, 1000, 5000, 10000]:
	 p_list = [n]
	for processor in [1, 2, 4, 8, 16]:
	 s = span_calc(n, processor, 2, lambda n: n)
	 p_list.append(s)
	 n_list.append(p_list)
	print_results_span(n_list)
