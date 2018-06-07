#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project from "Intro to Machine Learning" course from Udacity.
    Task: using a Naive Bayes Classifier identify emails by their authors

    number of data:
    Chris training emails: 7936
    Sara training emails: 7884

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()

### approximately training time: ~ 2.941 s
t0 = time()
clf.fit(features_train, labels_train)
print("training time:", round(time() - t0, 3), "s")

### approximately predicting time: ~ 0.516 s
t0 = time()
pred = clf.predict(features_test)
print("predicting time:", round(time() - t0, 3), "s")

### approximately accuracy ~0.97
from sklearn.metrics import accuracy_score

print(accuracy_score(pred, labels_test))


