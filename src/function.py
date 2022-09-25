def run(name):
    print(f'Hi, {name}')

    def func(name, job):
        print(name, 'is a', job)

    func(name='Bob', job='developer')
    # Prints Bob is a developer

    func(job='developer', name='Bob')
    # Prints Bob is a developer

    # Set default value 'developer' to a 'job' parameter
    def func(name, job='developer'):
        print(name, 'is a', job)

    func('Bob', 'manager')
    # Prints Bob is a manager

    def print_arguments(*args):
        print(args)

    print_arguments(1, 54, 60, 8, 98, 12)

    def print_arguments(**kwargs):
        print(kwargs)

    print_arguments(name='Bob', age=25, job='dev')
    # Prints {'name': 'Bob', 'age': 25, 'job': 'dev'}

    # Return addition and subtraction in a tuple
    def func(a, b):
        return a + b, a - b

    result = func(3, 2)

    def hello():
        """This function prints
           message on the screen"""
        print('Hello, World!')

    help(hello)

    import math
    x = math.sin(360 * 2 * math.pi)
    print(x)
    # Prints -3.133115067780141e-14

    def hello():
        print('Hello, World!')

    hi = hello
    hi()
    # Prints Hello, World!

    def findSquare(x):
        return x ** 2

    def findCube(x):
        return x ** 3

    # Create a dictionary of functions
    exponent = {'square': findSquare, 'cube': findCube}

    print(exponent['square'](3))
    # Prints 9
    print(exponent['cube'](3))
    # Prints 27

    x = 42  # global scope x

    def myfunc():
        x = 0
        print(x)  # local x is 0

    myfunc()
    print(x)  # global x is still 42

    # enclosing function
    def f1():
        x = 42

        # nested function
        def f2():
            nonlocal x
            x = 0
            print(x)  # x is now 0

        f2()
        print(x)  # x remains 0

    f1()

    doubler = lambda x: x * 2

    print(doubler(2))
    # Prints 4


if __name__ == '__main__':
    run('function')
