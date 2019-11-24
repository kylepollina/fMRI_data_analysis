from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
numFolds = 5

# returns a vector of 5 mean squared errors
def svm5F(X, y):
	#line to change for the other model
	clf = svm.SVC(gamma='scale', decision_function_shape='ovo')
	n, d = X.shape
	z = np.zeroes(numFolds)
	for i in range(numFolds):
		#get indices of the current fold
		startIndex = int(n * i / numFolds)
		endIndex = int(n * (i + 1) / numFolds)
		T = set(range(startIndex, endIndex))
		S = set(range(n)) - T #set difference

		#fit the model
		#line to change for the other model
		clf.fit(X[list(S)], y[list(S)])

		#for every incorrectly predicted point, increase the error for that point by 1
		z[i] = 0
		for t in T:
			if y[t] != clf.predict(X[t]):
				z[i] += 1
		#then divide by the number of test points for a weighted error
		z[t] /= len(T)

	return z

def knn5F(X, y, k):
	n, d = X.shape
	z = np.zeroes(numFolds)
	clf = KNeighborsClassifier(n_neighbors = k)
	for i in range(numFolds):
		#get indices of the current fold
		startIndex = int(n * i / numFolds)
		endIndex = int(n * (i + 1) / numFolds)
		T = set(range(startIndex, endIndex))
		S = set(range(n)) - T #set difference

		#fit the model
		clf.fit(X[list(S)], y[list(S)])

		#for every incorrectly predicted point, increase the error for that point by 1
		z[i] = 0
		for t in T:
			if y[t] != clf.predict(X[t]):
				z[i] += 1
		#then divide by the number of test points for a weighted error
		z[t] /= len(T)

	return z