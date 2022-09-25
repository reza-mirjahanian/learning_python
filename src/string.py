def run(name):
    print(f'Hi, {name}')
    S = 'ABCDEFGHI'
    print(S[0])    # Prints A
    S = 'ABCDEFGHI'
    print(S[2:5])
    S = 'Hello, world!'
    new_S = 'J' + S[1:]
    print(new_S)

    S = 'Hello,' " World!"
    print(S)
    S = ('Put strings within parentheses '
         'to join them together.')
    print(S)
    # the easy way
    S = '-' * 20

    L = ['red', 'green', 'blue', 'yellow']
    S = ','.join(L)
    print(S)
    S = 'Hello, World!'
    print('Hello' in S)

    S = 'Hello, World!'
    for letter in S:
        print(letter, end=' ')

    # raw string
    S = r'C:\new\text.txt'
    print(S)

    # printf-style % string formatting
    S = '%s is %d years old.' % ('Bob', 25)
    print(S)

    # format() Built-in Method
    S = '{1} is {0} years old.'.format(25, 'Bob')
    print(S)

    # f-String Formatter
    name = 'Bob'
    age = 25
    S = f"{name} is {age} years old."
    print(S)


if __name__ == '__main__':
    run('string')
