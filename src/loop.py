def run(name):
    print(f'Hi, {name}')
    x = 6
    while x:
        print(x)
        x -= 1
    # Prints 6 5 4 3 2 1

    x = 6
    while x:
        print(x)
        x -= 1
        if x == 3:
            break

    x = 6
    while x:
        print(x)
        x -= 1
    else:
        print('Done!')
    # Prints 6 5 4 3 2 1
    # Prints Done!

    # Skip 'blue'
    colors = ['red', 'green', 'blue', 'yellow']
    for x in colors:
        if x == 'blue':
            continue
        print(x)

    list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for sublist in list:
        for number in sublist:
            print(number)
    # Prints 1 2 3 4 5 6 7 8 9

    # Tuple unpacking
    T = [(1, 2), (3, 4), (5, 6)]
    for (a, b) in T:
        print(a, b)


if __name__ == '__main__':
    run('loop')
