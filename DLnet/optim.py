"""
We use optimizer to adjust the parameters
of the network based in the gradietns computed
during backpropagation
"""

from DLnet.nn import NeuralNet

class Optimizer:
    def step(self, net: NeuralNet) -> None:
        raise NotImplementedError


class SGD(Optimizer):
    def __init__(self, lr: float = 0.01) -> None:
        self.lr = lr

    def step(self, net: NeuralNet) -> None:
        for param, grad in net.param_and_grads():
            param -= self.lr * grad
