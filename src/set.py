def run(name):
    print(f'Hi, {name}')
    S = {'red', 'green', 'blue', 'red'}
    print(S)
    # A set itself is mutable (changeable), but it cannot contain mutable objects. Therefore,
    # immutable objects like numbers, strings, tuples can be a set item, but lists and dictionaries are mutable,
    # so they cannot be.
    S = {1, 'abc', ('a', 'b'), True}
    # S = {[1, 2], {'a': 1, 'b': 2}} !error

    # Set of items in an iterable
    S = set('abc')
    print(S)

    # You can add multiple items to a set using update() method.
    S = {'red', 'green', 'blue'}
    S.update(['yellow', 'orange'])
    print(S)

    # Union of the sets A and B is the set of all items in either A or B
    A = {'red', 'green', 'blue'}
    B = {'yellow', 'red', 'orange'}

    # by operator
    print(A | B)
    # Prints {'blue', 'green', 'yellow', 'orange', 'red'}

    # by method
    print(A.union(B))

    A = {'red', 'green', 'blue'}
    B = {'yellow', 'red', 'orange'}

    # by operator
    print(A & B)
    # Prints {'red'}

    # by method
    print(A.intersection(B))
    # Prints {'red'}

    # by operator
    print(A - B)
    # Prints {'blue', 'green'}

    # by method
    print(A.difference(B))
    
    # Set Symmetric Difference
    
    # by operator
    print(A ^ B)
    # Prints {'orange', 'blue', 'green', 'yellow'}

    # by method
    print(A.symmetric_difference(B))
    
    # Python Frozenset
    # S = frozenset({'red', 'green', 'blue'})
    # S.add('yellow')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run('Set')
