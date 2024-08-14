def elementwise_multiplication(vec_a, vec_b):
    assert (len(vec_a) == len(vec_b))
    return [vec_a[i] * vec_b[i] for i in range(len(a))]


def elementwise_addition(vec_a, vec_b):
    assert (len(vec_a) == len(vec_b))
    return [vec_a[i] + vec_b[i] for i in range(len(a))]


def vector_sum(vec_a):
    return sum(vec_a)


def vector_average(vec_a):
    return sum(vec_a) / len(vec_a)


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(elementwise_addition(a, b))
print(elementwise_multiplication(a, b))
print(vector_average(a))
print(vector_sum(a))
