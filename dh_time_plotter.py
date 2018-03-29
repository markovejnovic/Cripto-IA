import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

n = np.array([])
x = np.array([])
y = np.array([])

with open('dh_time.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)

	for row in reader:
		n = np.append(n, [int(row[0])])
		x = np.append(x, [float(row[1])])
		y = np.append(y, [float(row[2])])

print(n)
print(x)
print(y)

plt.figure()
plt.errorbar(n, x, yerr=np.std(x), fmt='x')
plt.plot(np.unique(n), np.poly1d(np.polyfit(n, x, 1))(np.unique(n)), 'r')
plt.xlabel("Magnitude of n")
plt.ylabel("Time required to calculate the private part X (s)")

plt.figure()
plt.errorbar(n, y, fmt='x')
plt.plot(n, y, 'r')
plt.xlabel("Magnitude of n")
plt.ylabel("Time required to calculate X from Y (s)")

plt.figure()
plt.errorbar(n, y - x, xerr=np.std(x), fmt='x')
plt.plot(n, y - x, 'r')
plt.xlabel("Magnitude of n")
plt.ylabel("The difference of time to calculate Y from X (s)")

plt.show()