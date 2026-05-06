def neural_network(inp, weight):
    return inp * weight


def get_error(prediction_true, prediction):
    return (prediction_true - prediction) ** 2


inp = 0.9
weight = 0.2

prediction_true = 0.2

for i in range(10):
    prediction = neural_network(inp, weight)
    error = get_error(prediction_true, prediction)
    print("Prediction: %.10f, Weight: %.5f, Error: %.20f" % (prediction, weight, error))
    delta = (prediction - prediction_true) * inp
    weight -= delta

"""функция ошибки представляет собой параболу, которая вычисляется по формуле:
                2
f(w) = (t - i w)
распишем формулу:
 2             2 2
t - 2 t i w + i w 
получим производную от формулы:
  2             2 2              2
(t - 2 t i w + i w )' = - 2 t + i w)
f'(w) = 2 i (i w - t)

Получаем:
i - входное значение
i * w - prediction (наш прогноз)
t - истинное значение
"""
