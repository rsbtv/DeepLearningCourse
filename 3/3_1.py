# Чистая сеть
weight = 0.1


def neural_network(input, weight):
    prediction = input * weight  # Умножение входного значения на весовой коэффициент
    return prediction


# передача одной точки данных
number_of_toes = [8.5, 9.5, 10, 9]
input = number_of_toes[0]
pred = neural_network(input, weight)  # Получение прогноза
print(pred)
