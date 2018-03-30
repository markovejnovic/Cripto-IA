import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from scipy.optimize import curve_fit

n = np.array([])
x = np.array([])
y = np.array([])

with open('rsa.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)

	for row in reader:
		n = np.append(n, [int(row[0])])
		x = np.append(x, [float(row[1])])
		y = np.append(y, [float(row[2])])

print(n)
print(x)
print(y)

plt.figure()
plt.errorbar(n, x, yerr=np.std(x), fmt='None')
plt.plot(np.unique(n), np.poly1d(np.polyfit(n, x, 1))(np.unique(n)), 'r')
plt.xlabel("Magnitude of n")
plt.ylabel("Time required to calculate p, q, n, d, e (s)")

plt.figure()
plt.errorbar(n, y)
plt.plot(n, y, 'r')
plt.xlabel("Magnitude of n")
plt.ylabel("Time required to factorize n (s)")

plt.figure()
plt.errorbar(n, y - x, xerr=np.std(x))
plt.plot(n, y - x, 'r')
plt.xlabel("Magnitude of n")
plt.ylabel("The difference of time required to factorize n and \nthe time required to calculate p, q, n, d, and e (s)")

plt.figure()
plt.plot(np.unique(n), np.poly1d(np.polyfit(n, x, 1))(np.unique(n)), 'r')
plt.plot(n, y - x, 'b')
plt.xlabel("Magnitude of n")
red_patch = mpatches.Patch(color="red", label="Time required to calculate p, q, n, d, e")
blue_patch = mpatches.Patch(color="blue", label="Time required to factorize n")
plt.legend(handles=[red_patch, blue_patch])

plt.show()