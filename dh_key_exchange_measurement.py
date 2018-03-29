import time
import random

Q = 13

def calculate_y(q, n, x):
	return q**x % n

def discrete_log(q, n, y):
	for i in range(0, n):
		if calculate_y(q, n, i) is y:
			return i

if __name__ == "__main__":
	print("n,Y time,Discrete Logarithm Time")
	i = 10**4
	while (i < 10**6):
		x = random.randint(0, 1000)

		y_start_time = time.process_time()
		calculate_y(Q, i, x)
		y_stop_time = time.process_time()

		log_start_time = time.process_time()
		discrete_log(Q, i, x)
		log_stop_time = time.process_time()

		print(str(i) + "," + str(y_stop_time - y_start_time) + "," + \
			str(log_stop_time - log_start_time))
		i += 1000