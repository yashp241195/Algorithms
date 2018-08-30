# Differntial Salary Distribution

x = [20,30,40,45,50]
y = [10,15,20,30,40]

tot_diffential = 0
tot_linear = 0

j = 0

xvals = []
ydiffvals = []
ylin = []

for i in range(x[len(x)-1]):

	tot_diffential += y[j]
	tot_linear += y[0]	
	
	if i == x[j]-1:
		j += 1

	xvals.append(i)
	ydiffvals.append(tot_diffential)
	ylin.append(tot_linear)

	# print(i,tot_diffential,tot_linear)


import matplotlib.pyplot as plt

plt.plot(xvals,ydiffvals)
plt.xlabel('sales')
plt.ylabel('differntials based salary')
plt.show()

