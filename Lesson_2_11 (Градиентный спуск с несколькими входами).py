import numpy as np

def neural_network(inp, weights):
    return inp.dot(weights)


def get_error(prediction_true, prediction):
    return (prediction_true - prediction) ** 2


inp = np.array([150, 40])
weights = np.array([0.2, 0.3])

prediction_true = 1
learning_rate = 0.00001

for i in range(300):
    prediction = neural_network(inp, weights)
    error = get_error(prediction_true, prediction)
    print("Prediction: %.10f, Weights: %s, Error: %.20f" % (prediction, weights, error))
    delta = (prediction - prediction_true) * inp * learning_rate
    weights -= delta
