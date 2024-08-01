def add(a, b):
    c = a + b
    d = a * b
    e = c * d
    f = a * b * e
    return f


x = 10
y = 20
z1 = x + y
z2 = x * y
result = add(z1, z2)
print(f"The result is {result}")
