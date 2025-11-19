'''
author : santoki het
github : @SantokiHet
organization : L.J University
'''

from train import *

class TestModel :
    def __init__(self) :
        self.pred = None
    
    def test(self) :
        self.y_pred = TrainModel().model.predict(TrainModel().X_test)

