def f(x):
    return x * 2

print(f(4))

for i in range(10):
    print('{0}:{1}'.format(i, f(i)), end=' ')
else:
    print()


for i in range(10):
    print('{0}:{1}'.format(i, (lambda x: x * 2)(i)), end=' ')
else:
    print()