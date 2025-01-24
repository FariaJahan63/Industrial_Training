n = 7

a, b = 0, 1
print("Fibonacci Series:", a, b, end=" ")

for _ in range(n - 2):
    c = a + b
    print(c, end=" ")
    a, b = b, c
