weight = 0.1
lr = 0.01


def neural_network(input, weight):
    prediction = input * weight
    return prediction


number_of_toes = [8.5]
win_or_lose_binary = [1]  # (победа!!!)

input = number_of_toes[0]
true = win_or_lose_binary[0]

pred = neural_network(input, weight)

error = (pred - true) ** 2
print(error)

# СРАВНЕНИЕ: Получение прогноза с увеличенным значением веса и вычисление ошибки
# Чтобы уменьшить ошикбку, нужно изменить вес. Попробуем сначала увеличить, а потом
# уменьшить его, передав в сеть weight+lr и weight-lr, и посмотрим,
# в каком случае получится самая низкая ошибка

lr = 0.1

p_up = neural_network(input, weight) + lr
e_up = (p_up - true) ** 2
print('UP: ', e_up)

p_dn = neural_network(input, weight) - lr
e_dn = (p_dn - true) ** 2
print('DOWN: ', e_dn)

if (error > e_dn or error > e_up):
    if (e_dn < e_up):
        weight -= lr
    if (e_up < e_dn):
        weight += lr
