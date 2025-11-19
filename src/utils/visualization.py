'''
author : Santoki Het
github : @SantokiHets
organization : L.J University
'''

import os
import sys
import matplotlib.pyplot as plt
from train import *

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Visualization :
    def __init__(self) :
        self.history = None

    def plot_loss(self):
        plt.plot(self.history.history['loss'],label='loss')
        plt.plot(self.history.history['val_loss'],label='val_loss')
        plt.legend()
        plt.savefig(os.path.join('/home/karan-chauhan/WorkStation/Project/Bank-Marketing-Campaign/results','loss-vs-val-loss'))
        # plt.show()
    
    def plot_accuracy(self):
        self.history = TrainModel().train()
        plt.plot(self.history.history['accuracy'],label='accuracy')
        plt.plot(self.history.history['val_accuracy'],label='val_accuracy')
        plt.legend()
        plt.savefig(os.path.join('/home/karan-chauhan/WorkStation/Project/Bank-Marketing-Campaign/results','accuracy-vs-val-accuracy'))
        # plt.show()
        self.plot_loss()


if __name__ == "__main__":
    Visualization().plot_accuracy()
