weights = [
    [0.1, 0.1, -0.3],  # травмы?
    [0.1, 0.2, 0.0],  # победа?
    [0.0, 1.3, 0.1]  # печаль?
]


def neural_network(input, weights):
    pred = vect_mat_mul(input, weights)
    return pred


def w_sum(a, b):
    assert (len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output


def vect_mat_mul(vect, matrix):
    assert (len(vect) == len(matrix))
    output = [0, 0, 0]

    for i in range(len(vect)):
        output[i] = w_sum(vect, matrix[i])

    return output


# Этот набор данных определяет текущее состояние перед началом каждой из первых четырех игр в сезоне:
toes = [8.5, 9.5, 9.9, 9.0]  # текущее среднее число игр, сыгранных игроками
wlrec = [0.65, 0.8, 0.8, 0.9]  # текущая доля игр, окончившихся победой (процент)
nfans = [1.2, 1.3, 0.5, 1.0]  # число болельщиков (в миллионах)

input = [toes[0], wlrec[0], nfans[0]]

pred = neural_network(input, weights)  # в переменной input передается запись, соответствующая первой игре в сезоне
