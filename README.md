DLnet is Neural Netowork implementation from scratch.
The first version contains the skeleton. It is inspired by Joel Gru's joelnet live coding.

Tasks to do:
* Add classes in layers module to take care of complex layers
* Currently optim module contains only SGD. Add more optimization algorithms.
* Refactor to include train in the nn object itself
* Add test module. Add splitting option for creating validation and test sets.
* Add callback functions to modify the training process.
* Add monotoring modules to check for the gradient weights performances.
* Implement a research paper (Not sure if this is a good idea unless I use GPU using architecture)