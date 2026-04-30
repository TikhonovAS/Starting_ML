# Создание простейшей нейросети

def neural_network(inp, weights):
    prediction = inp * weights
    return prediction


out_1 = neural_network(150, 0.2)
out_2 = neural_network(160, 0.2)

print(out_1)
print(out_2)
