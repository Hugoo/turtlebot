import numpy as np
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
from numpy import genfromtxt
import matplotlib.pyplot as plt

data = genfromtxt('positions_pan_tilt.txt', delimiter=',')[1:]

pan_tilt = data[:, [0,1]]
pan = data[:,0]
tilt = data[:,1]

scaler = StandardScaler()
scaler.fit(pan_tilt)
joblib.dump(scaler, 'src/cam_tracker/models/scaler.pkl', compress=1) 

pan_tilt_norm = scaler.transform(pan_tilt)

X = data[:,2]
Y = data[:,3]

clf_X = svm.SVR(C=20)
clf_X.fit(pan_tilt_norm, X)
joblib.dump(clf_X, 'src/cam_tracker/models/model-X.pkl', compress=1) 

clf_Y = svm.SVR(C=20)
clf_Y.fit(pan_tilt_norm, Y)
joblib.dump(clf_Y, 'src/cam_tracker/models/model-Y.pkl', compress=1) 
