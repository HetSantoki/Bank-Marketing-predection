'''
author : Santoki Het
github : @SantokiHet
organization : L.J University
'''

from test import *
from sklearn.metrics import classification_report 

class metrics :
    def __init__(self) :
        pass

    def accuracy(self) :

        y_pred = (TestModel().y_pred>0.5).astype(int)

        print(classification_report(TrainModel().y_test,y_pred))