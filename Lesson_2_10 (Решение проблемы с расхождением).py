def neural_network(inp, weight):
    return inp * weight


def get_error(prediction_true, prediction):
    return (prediction_true - prediction) ** 2


inp = 30                     # 0.9 - начальное значение
weight = 0.2

prediction_true = 70        # 0.2 - начальное значение
learning_rate = 0.001       # новый коэффициент для упорядочивания

for i in range(10):
    prediction = neural_network(inp, weight)
    error = get_error(prediction_true, prediction)
    print("Prediction: %.10f, Weight: %.5f, Error: %.20f" % (prediction, weight, error))
    delta = (prediction - prediction_true) * inp * learning_rate
    weight -= delta
