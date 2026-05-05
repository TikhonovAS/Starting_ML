import numpy as np

def neural_network(inp, weights):
    return inp.dot(weights)


def get_error(prediction_true, prediction):
    return (prediction_true - prediction) ** 2

prediction = neural_network(np.array([150, 40]), [0.2, 0.3])
prediction_true = 50
print(get_error(prediction_true, prediction))
