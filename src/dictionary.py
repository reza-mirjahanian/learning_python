def run(name):
    print(f'Hi, {name}')

    D = {'name': 'Bob',
         'age': 25,
         'job': 'Dev',
         'city': 'New York',
         'email': 'bob@web.com'}
    print(D)

    L = [('name', 'Bob'),
         ('age', 25),
         ('job', 'Dev')]

    D = dict(L)
    print(D)

    D = dict(name='Bob',
             age=25,
             job='Dev')

    print(D)

    keys = ['name', 'age', 'job']
    values = ['Bob', 25, 'Dev']

    D = dict(zip(keys, values))

    print(D)

    keys = ['a', 'b', 'c']
    defaultValue = 0

    D = dict.fromkeys(keys, defaultValue)

    print(D)
    # Prints {'a': 0, 'b': 0, 'c': 0}

    D1 = {'emp1': {'name': 'Bob', 'job': 'Mgr'},
          'emp2': {'name': 'Kim', 'job': 'Dev'}}

    D2 = {'emp2': {'name': 'Sam', 'job': 'Dev'},
          'emp3': {'name': 'Max', 'job': 'Janitor'}}

    D1.update(D2)

    print(D1)
    # Prints {'emp1': {'name': 'Bob', 'job': 'Mgr'},
    #         'emp2': {'name': 'Sam', 'job': 'Dev'},
    #         'emp3': {'name': 'Max', 'job': 'Janitor'}}

    D = {x: x ** 2 for x in range(5)}
    print(D)

    L = ['ReD', 'GrEeN', 'BlUe']
    D = {c.lower(): c.upper() for c in L}
    print(D)
    # Prints {'blue': 'BLUE', 'green': 'GREEN', 'red': 'RED'}

    # revert
    D = {0: 'red', 1: 'green', 2: 'blue'}
    R = {v: k for k, v in D.items()}
    print(R)
    # Prints {'red': 0, 'green': 1, 'blue': 2}




if __name__ == '__main__':
    run('dictionary')
