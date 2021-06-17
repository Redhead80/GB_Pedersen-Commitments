from random import randint
p = 11
q = 7
g = 3
s = randint(1, q-1)
h = g**s % p
print(h)


m = 6
r = randint(1, q-1)
c = ((g**m) * (h**r)) % p
print(c)

check = (g**m * h**r) % p
print("Пегги выиграла!") if check == c else "Попробуй снова!"