def run(name):
    print(f'Hi, {name}')
    x, y = 5, 5
    if x > y:
        print('x is greater')
    elif x < y:
        print('y is greater')
    else:
        print('x and y are equal')

    # Unlike other programming languages, Python does not have a ‘switch‘ statement.

    # Short Hand If - single statement
    x, y = 7, 5
    if x > y: print('x is greater'); print('y is smaller'); print('x and y are not equal')

    x, y = 7, 5

    max = x if x > y else y
    print(max)

if __name__ == '__main__':
    run('if-else')
