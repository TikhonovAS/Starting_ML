import numpy as np

def neural_network(inp, weights):
    return inp * weights


def get_error(prediction_true, prediction):
    return (prediction_true - prediction) ** 2


inp = 150
weights = np.array([0.2, 0.3])

predictions_true = np.array([[50, 120]])
learning_rate = 0.00001

for i in range(30):
    prediction = neural_network(inp, weights)
    error = get_error(predictions_true, prediction)
    print("Prediction: %s, Weights: %s, Error: %s" % (prediction, weights, error))
    delta = (prediction - predictions_true) * inp * learning_rate
    weights = weights - delta
