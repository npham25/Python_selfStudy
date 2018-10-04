

class LinearRegression(object):
	def mean(self,d):  #d is a list
		n = len(d)
		if n == 0: return None
		s = 0
		for i in d:
			s += i

		return s/n


	def variance(self, d): #d is a list
		m = self.mean(d)
		n = len(d)
		v = 0

		for i in d:
			v += (i - m) ** 2

		return v/(n-1)


	def estimated_parameters(self, x, Y):
		x_bar, Y_bar = self.mean(x), self.mean(Y)
		n = len(x)

		numerator, denominator, i = 0, 0, 0

		while i < n:
			numerator += (x[i] - x_bar) * (Y[i] - Y_bar)
			denominator += (x[i] - x_bar)**2
			i += 1
		
		if denominator == 0: return None

		b1 = numerator/denominator
		b0 = Y_bar - b1*x_bar

		return[b0, b1]


	def predict_Y(self, x, b0, b1): # d is a list
		result = [] # return a list of Y_predicted
		
		for i in x:
			result.append(round((b0 + b1 * i), 3))
		
		return result


	def SSR(self, x, Y, b0, b1):
		Y_bar = self.mean(Y)
		SSR = 0

		for i in x:
			SSR += ((b0 + b1*i) - Y_bar) ** 2

		return SSR


	def SST(self, Y): 
		Y_bar = self.mean(Y)
		SST = 0

		for j in Y:	
			SST += (j - Y_bar)**2

		return SST


	def R_square(self, x, Y, b0, b1):
		return round(self.SSR(x, Y, b0, b1)/self.SST(Y), 3)


	def coeff_var(self, x, Y, b0, b1):
		n = len(Y)
		SSE = self.SST(Y) - self.SSR(x, Y, b0, b1)
		MSE = SSE/(n-2)

		return round((MSE**0.5/self.mean(Y))*100,3)
		

	def ANOVA_table(self, x, Y, b0, b1):
		SSR = self.SSR(x, Y, b0, b1)
		SST = self.SST(Y)
		SSE = SST - SSR
		n = len(x)
		MSR = round(SSR/1, 3)
		MSE = round(SSE/(n-2), 3)

		print("Analysis of Variance")
		print("-----------------------------------------------------------------")
		print("%-20s %-10s %-20s %-20s" %("Source", "DF", "Sum of Squares", "Mean Squares"))
		print("-----------------------------------------------------------------")
		
		print("%-20s %-10s %-20s %-20s" %('Model', 1, round(SSR, 3), MSR))
		print("%-20s %-10s %-20s %-20s" %('Error', n-2, round(SSE, 3), MSE))
		print("%-20s %-10s %-20s %-20s" %('Corrected Total', n-1, round(SST, 3), ''))
		print("-----------------------------------------------------------------")

###################################################################################################################
def main():
	
	data = open("path", "r")
	x, Y = [], []
	for line in data:
		x.append(float(line.strip().split(",")[1]))
		Y.append(float(line.strip().split(",")[0]))

	model = LinearRegression()
		

	data.close()

	print("%-5s%-15s%-15s" %('', 'Mean', 'Var'))
	print("-----------------------------")
	print("%-5s%-15s%-15s" %('X', round(model.mean(x),3), round(model.variance(x),3)))
	print("%-5s%-15s%-15s" %('Y', round(model.mean(Y),3), round(model.variance(Y),3)))
	print()

	print("Least Squares Linear Regression:")
	print("--------------------------------")
	print()

	b = model.estimated_parameters(x, Y)
	print("Regression line: Y_hat =", round(b[0], 3), "+", round(b[1], 3),"X")
	print("R_Square:", model.R_square(x, Y, b[0], b[1]))
	print("Coefficient of Variation:", model.coeff_var(x, Y, b[0], b[1]))
	print()

	model.ANOVA_table(x, Y, b[0], b[1])
	print()

	print("Predict Y for X = [20, 22, 24, 26, 28]")
	print("Y = ", model.predict_Y([20, 22, 24, 26, 28], b[0], b[1]))
	print()

	print("Scatter plot")
	
main()
		




