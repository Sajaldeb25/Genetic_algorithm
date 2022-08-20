letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
i = 1
for l, n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    print(i)
    i = i+1