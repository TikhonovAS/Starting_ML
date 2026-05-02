def neural_network(inp, weights):
    prediction = [0, 0]
    for i in range(len(weights)):
        prediction[i] = inp * weights[i]
    return prediction


print(neural_network(0.65, [0.2, 0.1]))