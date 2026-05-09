import numpy as np


def neural_network(inp, weights):
    return inp.dot(weights)


def get_error(prediction_True, prediction):
    return (prediction_True - prediction) ** 2


inp = np.array([
    [150, 40],
    [140, 35],
    [155, 45],
    [185, 95],
    [145, 40],
    [195, 100],
    [180, 95],
    [170, 80],
    [160, 90]
])

weights = np.array([0.2, 0.3])

predictions_True = np.array([0, 0, 0, 100, 0, 100, 100, 100, 100])
learning_rate = 0.00001

count = 0

for i in range(500):          # cтохастический метод обучения
    error = 0
    for j in range(len(inp)):
        count += 1
        current_input = inp[j]
        prediction = neural_network(current_input, weights)
        prediction_True = predictions_True[j]
        error += get_error(prediction_True, prediction)
        print(count, "Prediction: %.10f, Prediction True: %.10f, Weights: %s" % (prediction, prediction_True, weights))
        delta = (prediction - prediction_True) * current_input * learning_rate
        weights -= delta

    print('Error: %.10f' % error)
    print('-------------------------------------------')

print(neural_network(np.array([150, 45]), weights))
print(neural_network(np.array([170, 75]), weights))