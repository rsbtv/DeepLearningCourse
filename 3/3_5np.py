import numpy as np

# игр % побед болельщиков
ih_wgt = np.array([
    [0.1, 0.2, -0.1],  # hid[0]
    [-0.1, 0.1, 0.9],  # hid[1]
    [0.1, 0.4, 0.1]  # hid[2]
]).T

# hid[0] hid[1] hid[2]
hp_wgt = np.array([
    [0.3, 1.1, -0.3],  # травмы?
    [0.1, 0.2, 0.0],  # победа?
    [0.0, 1.3, 0.1]  # печаль?
]).T

weights = [ih_wgt, hp_wgt]


def neural_network(input, weights):
    hid = input.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred


# Этот набор данных определяет текущее состояние перед началом каждой из первых четырех игр в сезоне:
toes = [8.5, 9.5, 9.9, 9.0]     # текущее среднее число игр, сыгранных игроками
wlrec = [0.65, 0.8, 0.8, 0.9]   # текущая доля игр, окончившихся победой (процент)
nfans = [1.2, 1.3, 0.5, 1.0]    # число болельщиков (в миллионах)

input = np.array([toes[0], wlrec[0], nfans[0]])

pred = neural_network(input, weights)
print(pred)