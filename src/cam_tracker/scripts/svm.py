# -*- coding: utf-8 -*-
from sklearn import linear_model
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
from sklearn.model_selection import GridSearchCV
import pickle

#Import data
#Get descriptors
X = pickle.load(open("X.p", 'rb'))
y = pickle.load(open("Y.p", 'rb'))
X = pd.DataFrame(np.float_(X), columns = ['timestamp', 'acc_x', 'acc_y', 'acc_z'])

y = pd.DataFrame(np.int_(y), columns = ['label'])
data = pd.concat([X,y], axis=1)
data = data[data.label.isin([1,2,3,4])]

#df = pd.read_csv('results.txt')
# create design matrix X and target vector y
#X = np.array(data.ix[:, 1:4]) 	# end index is exclusive
#y = np.array(data['label']) 	# another way of indexing a pandas df

print(np.shape(X))
#Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

svr = svm.SVC()
exponential_range = [pow(10, i) for i in range(-4, 1)]
parameters = {'kernel': ['linear', 'rbf'], 'C': exponential_range, 'gamma': exponential_range}
clf = GridSearchCV(svr, parameters, n_jobs=4, verbose=True)

clf.fit(X_train, y_train)

# predict the response
print("Starting prediction")
pred = clf.predict(X_test)
print("Pred", pred)

# evaluate accuracy
print(accuracy_score(y_test, pred))