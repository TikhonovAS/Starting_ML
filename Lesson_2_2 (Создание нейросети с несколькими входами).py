# Создание нейросети с несколькими входами

def neural_network(inp, weights):
    """Скалярное произведение"""
    prediction = 0
    for i in range(len (inp)):
        prediction += inp[i] * weights[i]
    return prediction


out_1 = neural_network([150, 40], [0.2, 0.3])
out_2 = neural_network([160, 70], [0.2, 0.3])

print(out_1)
print(out_2)
