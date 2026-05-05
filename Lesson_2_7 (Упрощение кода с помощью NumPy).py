# def neural_network(inp, weights): # Функция нейросети со скрытым слоем с несколькими входами и выходами
#     prediction_h = [0] * len(weights[0])
#     for i in range(len(weights[0])):
#         ws = 0
#         for j in range(len(inp)):
#             ws += inp[j] * weights[0][i][j]
#             prediction_h[i] = ws
#
#     prediction_out = [0] * len(weights[1])
#     for i in range(len(weights[1])):
#         ws = 0
#         for j in range(len(prediction_h)):
#             ws += prediction_h[j] * weights[1][i][j]
#             prediction_out[i] = ws
#
#     return prediction_out
# -------------------------------------------------------
#  Упрощение вышевыложенной функции
import numpy as np

def neural_network(inp, weights):
    prediction_h = inp.dot(weights[0])
    prediction_out = prediction_h.dot(weights[1])
    return prediction_out

inp = np.array([50, 165])
weights_h_1 = [0.2, 0.1]
weights_h_2 = [0.3, 0.1]

weights_out_1 = [0.4, 0.2]
weights_out_2 = [0.5, 0.3]

weights_h = np.array([weights_h_1, weights_h_2]).T
weights_out = np.array([weights_out_1, weights_out_2]).T

weights = [weights_h, weights_out]

print(neural_network(inp, weights))