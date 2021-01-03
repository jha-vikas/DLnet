"""
A loss function measures hwo good our predictions are
we can use this to adjust the parameters of our network
"""
import numpy as np
from DLnet.tensor import Tensor

class Loss:
    def loss(self, predcted: Tensor, actual: Tensor) -> float:
        raise NotImplementedError

    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        raise NotImplementedError



class MSE(Loss):
    """
    MSE is mean squared error, although we're just going
    to do the total squared error
    """
    def loss(self, predcted: Tensor, actual: Tensor) -> float:
        return np.sum((predcted - actual)**2)


    def grad(self, predicted: Tensor, actual: Tensor) -> Tensor:
        return 2 * (predicted - actual)